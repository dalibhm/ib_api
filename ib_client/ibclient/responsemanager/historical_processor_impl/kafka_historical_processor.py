from configparser import ConfigParser

from injector import inject

from ibapi.common import BarData

from responsemanager.historical_processor_impl.kafka_producer import KafkaProducer, format_data, format_data_end, \
    format_error
from responsemanager.historical_processor_impl.schemas.historical_end_schema import historical_data_end_key_schema_str, \
    historical_data_end_value_schema_str
from responsemanager.historical_processor_impl.schemas.historical_error_schema import historical_error_key_schema_str, \
    historical_error_value_schema_str
from responsemanager.historical_processor_impl.schemas.historical_schema import historical_data_key_schema_str, \
    historical_data_value_schema_str
from responsemanager.historical_processor import HistoricalDataProcessor


class KafkaHistoricalDataProcessor(HistoricalDataProcessor):
    @inject
    def __init__(self, config: ConfigParser):
        self.data_processor = KafkaProducer(topic=config.get('kafka', 'historical-data-responses-topic'),
                                            key_schema=historical_data_key_schema_str,
                                            value_schema=historical_data_value_schema_str,
                                            config=config)

        self.data_end_processor = KafkaProducer(topic=config.get('kafka', 'historical-data-end-topic'),
                                                key_schema=historical_data_end_key_schema_str,
                                                value_schema=historical_data_end_value_schema_str,
                                                config=config)

        self.error_processor = KafkaProducer(topic=config.get('kafka', 'historical-errors-topic'),
                                             key_schema=historical_error_key_schema_str,
                                             value_schema=historical_error_value_schema_str,
                                             config=config)

    def process_data(self, request_id, request, bar_data: BarData):
        key = {'requestId': request_id}
        formatted_data = format_data(request, bar_data)
        self.data_processor.send_msg(key, formatted_data)

    def process_data_end(self, request_id: int, request, start: str, end: str):
        key = {'requestId': request_id}
        formatted_data = format_data_end(request, start, end)
        self.data_end_processor.send_msg(key, formatted_data)

    def process_error(self, request_id: int, request, errorCode: int, errorString: str):
        key = {'requestId': request_id}
        formatted_data = format_error(request, errorCode, errorString)
        self.data_end_processor.send_msg(key, format_data_end(request, '19000101', '19000101'))
        self.error_processor.send_msg(key, formatted_data)
