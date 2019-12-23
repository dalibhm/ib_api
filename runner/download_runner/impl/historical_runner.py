import logging
import time
from datetime import datetime, timedelta

from exceptions import RequestFailed, DataAlreadyInDB
from request_scheduler import RequestScheduler
from request_templates.params import HistoricalRequestTemplate
from services.historical_data_service import HistoricalDataService

logger = logging.getLogger(__name__)


class HistoricalRunner:
    def __init__(self, start_date, end_date,
                 ib_client=None, historical_data_service=None):
        self.ib_client = ib_client
        self.historical_data_service: HistoricalDataService = historical_data_service
        self.start_date = start_date
        self.end_date = end_date

    def run(self, contract) -> None:
        start_date = self.start_date
        contract, arranged_params = self.validate_params(contract)
        if arranged_params:
            logger.info('sending - historical data request : {} {} {}'
                        .format(contract['symbol'], start_date, self.end_date))
            status = self.ib_client.request_historical_data(contract, arranged_params)
            logger.info('sent - historical data request : {} {} {}'
                        .format(contract['symbol'], start_date, self.end_date))
            logger.debug('request accounted for...')
            logger.info('status : {}'.format(status))
            if not status:
                raise RequestFailed
            else:
                logger.info('Historical data request sent : {} {} {}'
                            .format(contract['symbol'], start_date, self.end_date))
        else:
            raise DataAlreadyInDB

    def validate_params(self, contract):
        symbol = contract['symbol']
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d')

        latest_timestamp = self.historical_data_service.get_latest_timestamp(symbol, "%Y-%m-%d")
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
