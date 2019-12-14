import logging
from queue import Queue

import grpc

from exceptions import RequestFailed, EndOfTopic, NoMessage
from download_runner.impl.historical_end_reader import HistoricalEndReader
from download_runner.kafka_download_runner import KafkaDownloadRunner
from request_scheduler import RequestScheduler
from download_runner.impl.historical_runner import HistoricalRunner

logger = logging.getLogger(__name__)


class KafkaHistoricalDownloadRunner(KafkaDownloadRunner):
    """
    At the moment running multiple runners in the same process is not possible.
    Please run historical data separately from fundamental data for example.
    """

    def __init__(self, services,
                 start_date=None, end_date=None, config=None):
        self.services = services

        self.start_date = start_date
        self.end_date = end_date
        historical_runner = HistoricalRunner(self.start_date, self.end_date,
                                             self.services['ib'],
                                             self.services['historical_data']
                                             )
        super().__init__(runner=historical_runner, config=config)

        self.end_signal_queue = Queue()

        self.request_scheduler = RequestScheduler(config)

        self.historical_end_reader = HistoricalEndReader(self.end_signal_queue, self.request_scheduler, config)
        self.historical_end_reader.daemon = True

    def run(self):
        self.historical_end_reader.start()

        while True:
            if self.request_scheduler.poll_stock():
                try:
                    stock = self.stock_consumer.poll()
                except NoMessage:
                    continue
                except EndOfTopic:
                    break

                stock = modify_stock(stock)

                try:
                    self.runner.run(stock)
                    self.request_scheduler.request_added()
                except RequestFailed:
                    logger.info('historical request failed for {}'.format(stock))
                except grpc.RpcError as e:
                    logger.exception('GRPC error {}'.format(e.code()))


def modify_stock(stock):
    contract = {k: v for (k, v) in stock.items() if
                k in ['con_id', 'symbol', 'secType', 'exchange', 'currency']}
    contract['conId'] = contract.pop('con_id')
    return contract
