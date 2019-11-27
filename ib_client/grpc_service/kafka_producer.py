from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

value_schema_str = """
{
   "namespace": "historicalRequest",
   "name": "value",
   "type": "record",
   "fields" : [
     {
       "name" : "contract",
       "type" : "string"
     },
     {
       "name" : "endDateTime",
       "type" : "string"
     },
     {
       "name" : "durationString",
       "type" : "string"
     },
     {
       "name" : "barSizeSetting",
       "type" : "string"
     },
     {
       "name" : "whatToShow",
       "type" : "string"
     },
     {
       "name" : "useRTH",
       "type" : "int"
     },
     {
       "name" : "formatDate",
       "type" : "int"
     },
     {
       "name" : "keepUpToDate",
       "type" : "boolean"
     }
   ]
}
"""

key_schema_str = """
{
   "namespace": "historicalRequest",
   "name": "key",
   "type": "record",
   "fields" : [
     {
       "name" : "requestId",
       "type" : "int"
     }
   ]
}
"""


class KafkaRequestManager:
    def __init__(self, config):
        kafka_config = {
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            'schema.registry.url': config.get('kafka', 'schema.registry.url')
        }
        self.topic = config.get('kafka', 'historical-data-requests-topic')

        value_schema = avro.loads(value_schema_str)
        key_schema = avro.loads(key_schema_str)

        #self.producer = AvroProducer(config, default_value_schema=value_schema)
        self.producer = AvroProducer(kafka_config, 
                                     default_key_schema=key_schema, 
                                     default_value_schema=value_schema)

    def push_historical_request(self, requestId, request):
        v = {
            'contract': request.contract.symbol,
            'endDateTime': request.endDateTime,
            'durationString': request.durationString,
            'barSizeSetting': request.barSizeSetting,
            'whatToShow': request.whatToShow,
            'useRTH': request.useRTH,
            'formatDate': request.formatDate,
            'keepUpToDate': request.keepUpToDate
        }
        self.producer.produce(topic=self.topic,
                              value=v,
                              key={'requestId': requestId})
        self.producer.flush()
