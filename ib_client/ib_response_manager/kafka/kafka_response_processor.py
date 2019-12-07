from datetime import datetime

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer


from ib_response_manager.response_manager import ResponseManager
from proto.request_data_pb2 import HistoricalDataRequest

from requestmanager.requestmanager import RequestManager
from .historical_schema import historical_data_value_schema_str, historical_data_key_schema_str
from ib_response_manager.kafka.historical_end_schema import historical_data_end_value_schema_str, \
    historical_data_end_key_schema_str

from ibapi.common import BarData


class KafkaResponseManager(ResponseManager):
    def __init__(self, config, request_manager):
        kafka_config = {
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            'schema.registry.url': config.get('kafka', 'schema.registry.url')
        }
        self.historical_data_topic = config.get('kafka', 'historical-data-responses-topic')

        historical_data_value_schema = avro.loads(historical_data_value_schema_str)
        historical_data_key_schema = avro.loads(historical_data_key_schema_str)

        # self.producer = AvroProducer(config, default_value_schema=value_schema)
        self.historical_data_producer = AvroProducer(kafka_config,
                                                     default_key_schema=historical_data_key_schema,
                                                     default_value_schema=historical_data_value_schema)

        self.historical_data_end_topic = config.get('kafka', 'historical-data-end-topic')

        historical_data_end_value_schema = avro.loads(historical_data_end_value_schema_str)
        historical_data_end_key_schema = avro.loads(historical_data_end_key_schema_str)

        # self.producer = AvroProducer(config, default_value_schema=value_schema)
        self.historical_data_end_producer = AvroProducer(kafka_config,
                                                         default_key_schema=historical_data_end_key_schema,
                                                         default_value_schema=historical_data_end_value_schema)

        self.request_manager: RequestManager = request_manager

    def process_contract_details(self, request_id, contract_details):
        print(request_id, contract_details)

    def process_historical_data(self, requestId: int, bar_data: BarData):
        # print(requestId, bar_data)
        request: HistoricalDataRequest = self.request_manager.get_request_by_id(requestId)
        r = {
            'symbol': request.contract.symbol,
            # 'secType': request.contract.secType,
            # this field id probably empty because it is supposed to be read from the contract table, which
            # is not used for now, keep in mind
            'secType': 'STK',
            'exchange': request.contract.exchange,
            'currency': request.contract.currency,
            'barSize': request.barSizeSetting,
            'whatToShow': request.whatToShow,
            'useRTH': request.useRTH
        }
        r.update(bar_data.__dict__)

        # data = bar_data.__dict__
        # data['date'] = datetime.strptime(data['date'], "%Y%m%d").date()
        self.historical_data_producer.produce(topic=self.historical_data_topic,
                                              value=r,
                                              key={'requestId': requestId}
                                              )
        self.historical_data_producer.flush()

    def process_historical_data_end(self, requestId: int, start: str, end: str):
        # print(requestId, bar_data)
        request: HistoricalDataRequest = self.request_manager.get_request_by_id(requestId)
        r = {
            'symbol': request.contract.symbol,
            # 'secType': request.contract.secType,
            # this field id probably empty because it is supposed to be read from the contract table, which
            # is not used for now, keep in mind
            'secType': 'STK',
            'exchange': request.contract.exchange,
            'currency': request.contract.currency,
            'barSize': request.barSizeSetting,
            'whatToShow': request.whatToShow,
            'useRTH': request.useRTH
        }
        r.update({'start': start, 'end': end})

        self.historical_data_end_producer.produce(topic=self.historical_data_end_topic,
                                              value=r,
                                              key={'requestId': requestId}
                                              )
        self.historical_data_end_producer.flush()

    def process_financial_data(self, request, xml_data):
        print('TestResponseProcessor::from process_financial_data')
        print(request, xml_data)
