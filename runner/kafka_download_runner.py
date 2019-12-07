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


class KafkaDownloadRunner:
    """
    At the moment running multiple runners in the same process is not possible.
    Please run historical data separately from fundamental data for example.
    """

    def __init__(self, services, historical, fundamental, start_date, end_date, stock_number, config=None):
        self.services = services

        self.historical = historical
        self.fundamental = fundamental
        self.start_date = start_date
        self.end_date = end_date
        self.max_counter = stock_number
        if not self.historical and not self.fundamental:
            exit('nothing to run --> exiting program')
        self.threads = []

        # self.consumer = AvroConsumer(config.get('runner-kafka-config'))
        self.kafka_config = {
            "api.version.request": True,
            "enable.auto.commit": True,
            "enable.auto.offset.store": False,
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            "group.id": 'runner.group1',
            'schema.registry.url': config.get('kafka', 'schema.registry.url'),
            # the consumer was not running without default.topic.config
            "default.topic.config": {"auto.offset.reset": "earliest"}
        }
        self.consumer = AvroConsumer(self.kafka_config)
        self.topic = config.get('kafka', 'stocks-topic')
        self.consumer.subscribe([self.topic])

        self.historical_data_end_consumer = AvroConsumer(self.kafka_config)
        self.historical_data_end_topic = config.get('kafka', 'historical-data-end-topic')
        self.historical_data_end_consumer.subscribe([self.historical_data_end_topic])

        self.msg_queue = Queue()
        self.historical_data_end_queue = Queue()
        self.request_scheduler = RequestScheduler()


    def go(self):
        self.start()
        counter = 0
        logger.debug('polling data from kafka topic {} on {}'.format(self.topic, self.kafka_config['bootstrap.servers']))
        while True:
            if not self.request_scheduler.send() and counter > self.max_counter:
                continue
            self.poll_stock()
            counter += 1
            try:
                self.poll_historical_data_end()
            except:
                logger.exception('exception polling data from historical_data_end')

        for thread in self.threads:
            thread.join()

    def start(self):
        if self.historical:
            historical_runner = HistoricalRunner(self.services['ib'],
                                                 self.services['historical_data'],
                                                 self.msg_queue,
                                                 self.historical_data_end_queue,
                                                 self.start_date, self.end_date)
            historical_runner.start()
            self.threads.append(historical_runner)
            historical_end_reader = HistoricalEndReader(self.historical_data_end_queue, self.request_scheduler)
            historical_end_reader.start()
            self.threads.append(historical_end_reader)
        if self.fundamental:
            fundamental_runner = FundamentalRunner(self.services['ib'], self.msg_queue)
            fundamental_runner.start()
            self.threads.append(fundamental_runner)

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