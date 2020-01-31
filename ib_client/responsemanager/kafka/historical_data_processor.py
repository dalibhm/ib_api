from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

from responsemanager.historical_processor_impl.schemas.historical_schema import historical_data_value_schema_str, \
    historical_data_key_schema_str
from proto.request_data_pb2 import HistoricalDataRequest

from ibapi.common import BarData

from requestmanager.requestmanager import RequestManager


class HistoricalDataProcessor:
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

        self.request_manager: RequestManager = request_manager

    def produce_msg(self, request_id, request: HistoricalDataRequest, bar_data: BarData):
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
                                              key={'requestId': request_id}
                                              )
        self.historical_data_producer.flush()