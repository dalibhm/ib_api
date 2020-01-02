from responsemanager.kafka.historical_data_end_processor import HistoricalDataEndProcessor
from responsemanager.kafka.historical_data_processor import HistoricalDataProcessor
from responsemanager.kafka.historical_error_processor import HistoricalErrorProcessor
from responsemanager.response_manager import ResponseManager


from ibapi.common import BarData


class KafkaResponseManager(ResponseManager):
    def __init__(self, config, request_manager):
        self.historical_data_processor = HistoricalDataProcessor(config, request_manager)
        self.historical_data_end_processor = HistoricalDataEndProcessor(config, request_manager)
        self.error_processor = HistoricalErrorProcessor(config, request_manager)

    def process_contract_details(self, request_id, contract_details):
        print(request_id, contract_details)

    def process_historical_data(self, request_id, request, bar_data: BarData):
        self.historical_data_processor.produce_msg(request_id, request, bar_data)

    def process_historical_data_end(self, requestId: int, request, start: str, end: str):
        self.historical_data_end_processor.produce_msg(requestId, request, start, end)

    def process_historical_error(self, requestId: int, request, errorCode: int, errorString: str):
        self.historical_data_end_processor.produce_msg(requestId, request, '19000101', '19000101')
        self.error_processor.produce_msg(requestId, errorCode, errorString)

    def process_fundamental_data(self, request, xml_data):
        print('TestResponseProcessor::from process_financial_data')
        print(request, xml_data)
