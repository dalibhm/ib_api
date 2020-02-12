from ibapi.common import SetOfFloat, SetOfString
from injector import inject

from responsemanager.contract_details_processor import ContractDetailsProcessor
from responsemanager.fundamental_processor import FundamentalDataProcessor
from responsemanager.historical_processor import HistoricalDataProcessor
from responsemanager.option_params_processor import OptionParamsProcessor


class ResponseManager:
    @inject
    def __init__(self,
                 historical_data_processor: HistoricalDataProcessor,
                 fundamental_data_processor: FundamentalDataProcessor,
                 contract_details_processor: ContractDetailsProcessor,
                 option_params_processor: OptionParamsProcessor
                 ):
        self.historical_data_processor = historical_data_processor
        self.fundamental_data_processor = fundamental_data_processor
        self.contract_details_processor = contract_details_processor
        self.option_params_processor = option_params_processor

    ####################
    # fundamental data #
    ####################
    def process_fundamental_data(self, request_id, request, xml_data):
        self.fundamental_data_processor.process_data(request_id, request, xml_data)

    def process_fundamental_data_error(self, request_id, request, error_code, error_string):
        self.fundamental_data_processor.process_error(request_id, request, error_code, error_string)

    ####################
    # historical data  #
    ####################
    def process_historical_data(self, request_id, request, bar_data):
        self.historical_data_processor.process_data(request_id, request, bar_data)

    def process_historical_data_end(self, request_id, request, start, end):
        self.historical_data_processor.process_data_end(request_id, request, start, end)

    def process_historical_data_error(self, request_id, request, error_code, error_string):
        self.historical_data_processor.process_error(request_id, request, error_code, error_string)

    ####################
    # contracts data   #
    ####################
    def process_contract_details(self, request_id, request, contract_details):
        self.contract_details_processor.process_data(request_id, request, contract_details)

    def process_contract_details_end(self, request_id, request):
        self.contract_details_processor.process_data_end(request_id, request)
        
    def process_contract_details_error(self, request_id, request, error_code, error_string):
        self.contract_details_processor.process_error(request_id, request, error_code, error_string)

    ####################
    # options params   #
    ####################

    def process_option_params(self, request_id, request, exchange: str,
                              underlyingConId: int, tradingClass: str, multiplier: str,
                              expirations: SetOfString, strikes: SetOfFloat):
        self.option_params_processor.process_data(request_id, request, exchange, underlyingConId,
                                                  tradingClass, multiplier, expirations, strikes)

    def process_option_params_end(self, request_id, request):
        self.option_params_processor.process_data_end(request_id, request)
