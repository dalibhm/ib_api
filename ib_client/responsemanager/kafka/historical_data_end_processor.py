from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

from requestmanager.requestmanager import RequestManager
from responsemanager.historical_processor_impl.schemas.historical_end_schema import historical_data_end_value_schema_str, \
    historical_data_end_key_schema_str


class HistoricalDataEndProcessor:
    def __init__(self, config, request_manager):
        kafka_config = {
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            'schema.registry.url': config.get('kafka', 'schema.registry.url')
        }

        self.historical_data_end_topic = config.get('kafka', 'historical-data-end-topic')

        historical_data_end_value_schema = avro.loads(historical_data_end_value_schema_str)
        historical_data_end_key_schema = avro.loads(historical_data_end_key_schema_str)

        # self.producer = AvroProducer(config, default_value_schema=value_schema)
        self.historical_data_end_producer = AvroProducer(kafka_config,
                                                         default_key_schema=historical_data_end_key_schema,
                                                         default_value_schema=historical_data_end_value_schema)

        self.request_manager: RequestManager = request_manager

    def produce_msg(self, requestId: int, request, start: str, end: str):
        # print(requestId, bar_data)
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

