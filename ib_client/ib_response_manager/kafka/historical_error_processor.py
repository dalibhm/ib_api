from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer


from proto.request_data_pb2 import HistoricalDataRequest

from requestmanager.requestmanager import RequestManager
from ib_response_manager.kafka.schemas.historical_error_schema import historical_error_key_schema_str, \
    historical_error_value_schema_str


class HistoricalErrorProcessor:
    def __init__(self, config, request_manager):
        kafka_config = {
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            'schema.registry.url': config.get('kafka', 'schema.registry.url')
        }
        self.error_topic = config.get('kafka', 'historical-errors-topic')

        error_value_schema = avro.loads(historical_error_value_schema_str)
        error_key_schema = avro.loads(historical_error_key_schema_str)

        # self.producer = AvroProducer(config, default_value_schema=value_schema)
        self.error_producer = AvroProducer(kafka_config,
                                           default_key_schema=error_key_schema,
                                           default_value_schema=error_value_schema)

        self.request_manager: RequestManager = request_manager

    def produce_msg(self, requestId: int, errorCode: int, errorString: str):
        request: HistoricalDataRequest = self.request_manager.get_request_by_id(requestId)['request']
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
        r.update({"errorCode": errorCode, "errorString": errorString})

        # data = bar_data.__dict__
        # data['date'] = datetime.strptime(data['date'], "%Y%m%d").date()
        self.error_producer.produce(topic=self.error_topic,
                                    value=r,
                                    key={'requestId': requestId}
                                    )
        self.error_producer.flush()