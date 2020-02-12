from configparser import ConfigParser

from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

from proto.request_data_pb2 import HistoricalDataRequest


def prepare_record(request: HistoricalDataRequest):
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
    return r


def format_data(request, bar_data):
    r = prepare_record(request)
    r.update(bar_data.__dict__)
    return r


def format_data_end(request, start, end):
    r = prepare_record(request)
    r.update({'start': start, 'end': end})
    return r


def format_error(request, errorCode, errorString):
    r = prepare_record(request)
    r.update({"errorCode": errorCode, "errorString": errorString})
    return r


class KafkaProducer:
    def __init__(self, topic, key_schema, value_schema, config: ConfigParser):
        self._topic = topic

        kafka_config = {
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            'schema.registry.url': config.get('kafka', 'schema.registry.url')
        }

        value_schema = avro.loads(value_schema)
        key_schema = avro.loads(key_schema)

        self._producer = AvroProducer(kafka_config,
                                      default_key_schema=key_schema,
                                      default_value_schema=value_schema)

    def send_msg(self, key, value):
        self._producer.produce(topic=self._topic,
                               value=value,
                               key=key
                               )
        self._producer.flush()
