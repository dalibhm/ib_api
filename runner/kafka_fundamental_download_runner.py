import logging
import time
from queue import Queue

from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer

from fundamental_runner import FundamentalRunner

logger = logging.getLogger(__name__)


class KafkaFundamentalDownloadRunner:
    """
    At the moment running multiple runners in the same process is not possible.
    Please run historical data separately from fundamental data for example.
    """

    def __init__(self, services, stock_number=None, config=None):
        self.services = services

        self.max_counter = stock_number or 10

        self.threads = []

        self.kafka_config = {
            "api.version.request": True,
            "enable.auto.commit": True,
            "enable.auto.offset.store": False,
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            "group.id": 'runner.fundamental.group',
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
        time.sleep(2)
        counter = 0
        logger.info('polling data from kafka topic {} on {}'.format(self.topic, self.kafka_config['bootstrap.servers']))
        while True:
            if counter < self.max_counter:
                self.poll_stock()
                counter += 1

        for thread in self.threads:
            thread.join()

    def start(self):
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
