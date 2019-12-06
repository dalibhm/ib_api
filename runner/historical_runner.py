import logging
import time
from threading import Thread

from request_templates.params import HistoricalRequestTemplate
from services.historical_data_service import HistoricalDataService

logger = logging.getLogger(__name__)


class HistoricalRunner(Thread):
    def __init__(self, ib_client, historical_data_service, msg_queue, start_date, end_date):
        super().__init__()
        self.ib_client = ib_client
        self.historical_data_service: HistoricalDataService = historical_data_service
        self.msg_queue = msg_queue
        self.start_date = start_date
        self.end_date = end_date

    def run(self) -> None:
        start_date = self.start_date
        try:
            logger.debug('starting historical runner loop')
            while self.msg_queue:
                contract = self.msg_queue.get()
                latest_timestamp = self.historical_data_service.get_latest_timestamp(contract['symbol'], "%Y-%m-%d")
                if latest_timestamp:
                    start_date = latest_timestamp
                params = {
                    "start_date": start_date,  # "1999-01-01",
                    "end_date": self.end_date,  # "2019-11-27",
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
