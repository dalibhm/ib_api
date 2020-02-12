import logging
import grpc
from confluent_kafka.cimpl import KafkaException

from runner.exceptions import RequestFailed, EndOfTopic, NoMessage
from request_scheduler import RequestScheduler
from download_runner.impl.kafka_consumer import KafkaConsumer

logger = logging.getLogger(__name__)


class KafkaDownloadRunner:
    """
    At the moment running multiple runners in the same process is not possible.
    Please run historical data separately from fundamental data for example.
    """

    def __init__(self, runner, config=None):
        self.runner = runner

        self.request_scheduler = RequestScheduler(config)

        self.stock_consumer = KafkaConsumer(group_id='runner.historical.group',
                                            topic=config.get('kafka', 'stocks-topic'),
                                            default_topic_config={"auto.offset.reset": "earliest"},
                                            config=config)

    def run(self):
        while True:
            try:
                stock = self.stock_consumer.poll()
            except NoMessage:
                continue
            except EndOfTopic:
                break
            except KafkaException:
                continue
            except:
                logger.exception('unexpected exception')

            stock = modify_stock(stock)

            try:
                self.runner.run(stock)
            except RequestFailed:
                logger.info('request failed for {}'.format(stock))
            except grpc.RpcError as e:
                logger.exception('GRPC error {}'.format(e.code()))


def modify_stock(stock):
    contract = {k: v for (k, v) in stock.items() if
                k in ['con_id', 'symbol', 'secType', 'exchange', 'currency']}
    contract['conId'] = contract.pop('con_id')
    return contract
