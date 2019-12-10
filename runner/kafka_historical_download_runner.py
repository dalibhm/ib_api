import logging
import time
from queue import Queue
from threading import Thread

from download_manager.download_config import DownloadConfigFactory
from download_manager.download_manager_factory import DownloadManagerFactory
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer

from fundamental_runner import FundamentalRunner
from historical_en_reader import RequestScheduler, HistoricalEndReader
from historical_runner import HistoricalRunner
from request_templates.params import HistoricalRequestTemplate

logger = logging.getLogger(__name__)


class KafkaHistoricalDownloadRunner:
    """
    At the moment running multiple runners in the same process is not possible.
    Please run historical data separately from fundamental data for example.
    """

    def __init__(self, services,
                 start_date=None, end_date=None, stock_number=None, config=None):
        self.services = services

        self.start_date = start_date
        self.end_date = end_date
        self.max_counter = stock_number or 10
        self.threads = []

        self.kafka_config = {
            "api.version.request": True,
            "enable.auto.commit": True,
            "enable.auto.offset.store": False,
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            "group.id": 'runner.historical.group',
            'schema.registry.url': config.get('kafka', 'schema.registry.url'),
            # the consumer was not running without default.topic.config
            "default.topic.config": {"auto.offset.reset": "earliest"}
        }
        self.consumer = AvroConsumer(self.kafka_config)
        self.topic = config.get('kafka', 'stocks-topic')
        self.consumer.subscribe([self.topic])

        self.kafka_config["default.topic.config"] = {"auto.offset.reset": "latest"}
        self.kafka_config["group.id"] = {"hist.data.end.group"}
        self.historical_data_end_consumer = AvroConsumer(self.kafka_config)
        self.historical_data_end_topic = config.get('kafka', 'historical-data-end-topic')
        self.historical_data_end_consumer.subscribe([self.historical_data_end_topic])

        self.msg_queue = Queue()
        self.historical_data_end_queue = Queue()
        self.request_scheduler = RequestScheduler()

    def go(self):
        self.start()
        time.sleep(2)
        counter = 0
        logger.info('polling data from kafka topic {} on {}'.format(self.topic, self.kafka_config['bootstrap.servers']))
        while True:
            try:
                self.poll_historical_data_end()
            except:
                pass
            if not self.request_scheduler.send() or counter > self.max_counter:
                continue
            logger.info('{} active requests'.format(self.request_scheduler.active_requests))
            self.poll_stock()
            counter += 1

        for thread in self.threads:
            thread.join()

    def start(self):
        historical_runner = HistoricalRunner(self.start_date, self.end_date,
                                             self.services['ib'],
                                             self.services['historical_data'],
                                             self.request_scheduler,
                                             self.msg_queue
                                             )
        historical_runner.start()
        self.threads.append(historical_runner)
        historical_end_reader = HistoricalEndReader(self.historical_data_end_queue, self.request_scheduler)
        historical_end_reader.start()
        self.threads.append(historical_end_reader)

    def poll_stock(self):
        msg = self.consumer.poll(0.1)
        if msg is None:
            return
        elif not msg.error():
            logger.info('Received message: {}'.format(msg.value()))
            contract = {k: v for (k, v) in msg.value().items() if
                        k in ['con_id', 'symbol', 'secType', 'exchange', 'currency']}
            contract['conId'] = contract.pop('con_id')
            #            if contract['symbol'] in TO_SKIP:
            #                return
            self.msg_queue.put(contract)
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            logger.info('End of partition reached {0}/{1}'.format(msg.topic(), msg.partition()))
        else:
            logger.error('Error occured in Kafka: {0}'.format(msg.error().str()))

    def poll_historical_data_end(self):
        msg = self.historical_data_end_consumer.poll(0.1)
        if msg is None:
            return
        elif not msg.error():
            logger.info('historical_data_end: {}'.format(msg.value()))
            self.historical_data_end_queue.put(msg.value())
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            logger.info('End of partition reached {0}/{1}'.format(msg.topic(), msg.partition()))
        else:
            logger.error('Error occured in Kafka: {0}'.format(msg.error().str()))
