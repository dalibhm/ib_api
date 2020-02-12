import logging
from datetime import datetime

from injector import inject

from download_runner.historical_params import HistoricalParams
from exceptions import DataAlreadyInDB
from request_templates.params import HistoricalRequestTemplate

from services.ib_client import IbClient

from historical_data.adjust_request_dates import adjust_request_dates
from historical_data import HistoricalDataService

logger = logging.getLogger(__name__)


class HistoricalRunner:
    @inject
    def __init__(self, historical_params: HistoricalParams,
                 ib_client: IbClient = None,
                 historical_data_service: HistoricalDataService = None):
        self.ib_client = ib_client
        self.historical_data_service: HistoricalDataService = historical_data_service
        self.start_date = historical_params.start_date
        self.end_date = historical_params.end_date

    def run(self, contract) -> None:
        start_date = self.start_date
        contract, arranged_params = self.adjust_params(contract)
        if arranged_params:
            logger.info('sending - historical data request : {} {} {}'
                        .format(contract['symbol'], start_date, self.end_date))
            status = self.ib_client.request_historical_data(contract, arranged_params)
            logger.info('status {} - historical data request : {} {} {}'
                        .format(contract['symbol'], start_date, self.end_date, status))
        else:
            raise DataAlreadyInDB

    def adjust_params(self, contract):
        symbol = contract['symbol']
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d')
        start_db = self.historical_data_service.get_start_db(symbol, "%Y-%m-%d")
        end_db = self.historical_data_service.get_end_db(symbol, "%Y-%m-%d")

        if len(start_db) > 0:
            request_start, request_end = adjust_request_dates(start_date,
                                                          end_date,
                                                          datetime.strptime(start_db, '%Y-%m-%d'),
                                                          datetime.strptime(end_db, '%Y-%m-%d'))
        else:
            request_start, request_end = (start_date, end_date)


        params = {
            "start_date": request_start.strftime('%Y%m%d'),  # "1999-01-01",
            "end_date": request_end.strftime('%Y%m%d'),  # "2019-11-27",
            "bar_size": "1 day",
            "price_type": "TRADES"
        }
        params_manager = HistoricalRequestTemplate(params)
        arranged_params = params_manager.get_ib_params()
        contract['exchange'] = 'SMART'
        return contract, arranged_params
