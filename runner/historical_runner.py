import logging
import time
from threading import Thread

from request_templates.params import HistoricalRequestTemplate

logger = logging.getLogger(__name__)


class HistoricalRunner(Thread):
    def __init__(self, ib_client, msg_queue):
        super().__init__()
        self.ib_client = ib_client
        self.msg_queue = msg_queue

    def run(self) -> None:
        try:
            logger.debug('starting historical runner loop')
            while self.msg_queue:
                contract = self.msg_queue.get()
                params = {
                    "start_date": "1999-01-01",
                    "end_date": "2019-11-27",
                    "bar_size": "1 day",
                    "price_type": "TRADES"
                }
                arranged_params = HistoricalRequestTemplate(params).params
                contract['exchange'] = 'SMART'
                self.ib_client.request_historical_data(contract, arranged_params)
                time.sleep(0.1)
                self.msg_queue.task_done()
        except:
            logger.exception('unhandled exception in HistoricalRunner')
