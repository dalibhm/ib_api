import logging
import time
from queue import Queue
from threading import Thread

from download_manager.download_config import DownloadConfigFactory
from download_manager.download_manager_factory import DownloadManagerFactory
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer

from fundamental_runner import FundamentalRunner
from historical_runner import HistoricalRunner
from request_templates.params import HistoricalRequestTemplate

MAX_COUNTER = 168624

logger = logging.getLogger(__name__)


class KafkaDownloadRunner:
    """
    At the moment running multiple runners in the same process is not possible.
    Please run historical data separately from fundamental data for example.
    """

    def __init__(self, services, historical, fundamental, config=None):
        self.services = services

        self.historical = historical
        self.fundamental = fundamental

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

        self.msg_queue = Queue()

    def go(self):
        self.start()
        counter = 0
        logger.debug('polling data from kafka topic {} on {}'.format(self.topic, self.kafka_config['bootstrap.servers']))
        while True and counter < MAX_COUNTER:
            self.poll()
            counter += 1

        # self.pull()
        for thread in self.threads:
            thread.join()

    def start(self):
        if self.historical:
            historical_runner = HistoricalRunner(self.services['ib'], self.msg_queue)
            historical_runner.start()
            self.threads.append(historical_runner)
        if self.fundamental:
            fundamental_runner = FundamentalRunner(self.services['ib'], self.msg_queue)
            fundamental_runner.start()
            self.threads.append(fundamental_runner)

    def poll(self):
        msg = self.consumer.poll(10)
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
