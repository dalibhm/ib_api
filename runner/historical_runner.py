import logging
import time
from datetime import datetime, timedelta
from threading import Thread

from historical_en_reader import RequestScheduler
from request_templates.params import HistoricalRequestTemplate
from services.historical_data_service import HistoricalDataService

logger = logging.getLogger(__name__)


class HistoricalRunner(Thread):
    def __init__(self, start_date, end_date,
                 ib_client=None, historical_data_service=None, request_scheduler=None, msg_queue=None):
        super().__init__()
        self.ib_client = ib_client
        self.historical_data_service: HistoricalDataService = historical_data_service
        self.request_scheduler: RequestScheduler = request_scheduler
        self.msg_queue = msg_queue
        self.start_date = start_date
        self.end_date = end_date

    def run(self) -> None:
        try:
            logger.debug('starting historical runner loop')
            while self.msg_queue:
                if not self.msg_queue.empty():
                    try:
                        start_date = self.start_date
                        contract = self.msg_queue.get()
                        contract, arranged_params = self.validate_params(contract)
                        if arranged_params:
                            logger.info('sending - historical data request : {} {} {}'
                                        .format(contract['symbol'], start_date, self.end_date))
                            status = self.ib_client.request_historical_data(contract, arranged_params)
                            logger.info('sent - historical data request : {} {} {}'
                                        .format(contract['symbol'], start_date, self.end_date))
                            self.request_scheduler.request_added()
                            logger.debug('request accounted for...')
                            logger.info('status : {}'.format(status))
                            if not status:
                                self.request_scheduler.request_ended()
                                logger.debug('{} request removed because unsuccessful'.format(contract['symbol']))

                            self.msg_queue.task_done()
                            logger.info('Historical data request sent : {} {} {}'
                                        .format(contract['symbol'], start_date, self.end_date))
                    except:
                        logger.exception('exception while sending historical request'.format(contract['symbol']))
        except:
            logger.exception('unhandled exception in HistoricalRunner for {}'.format(contract['symbol']))

    def validate_params(self, contract):
        symbol = contract['symbol']
        latest_timestamp = self.historical_data_service.get_latest_timestamp(symbol, "%Y-%m-%d")
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d')

        if latest_timestamp:
            latest = datetime.strptime(latest_timestamp, '%Y-%m-%d')
            if latest >= end_date - timedelta(days=1):
                logger.info('latest data already ib database for {}'.format(symbol))
                return contract, None
            elif start_date >= end_date - timedelta(days=1):
                start_date = latest

        params = {
            "start_date": start_date.strftime('%Y%m%d'),  # "1999-01-01",
            "end_date": end_date.strftime('%Y%m%d'),  # "2019-11-27",
            "bar_size": "1 day",
            "price_type": "TRADES"
        }
        params_manager = HistoricalRequestTemplate(params)
        arranged_params = params_manager.get_ib_params()
        contract['exchange'] = 'SMART'
        return contract, arranged_params
