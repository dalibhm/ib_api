# from confluent_kafka import avro
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
config = {
    "api.version.request": True,
    "enable.auto.commit": True,
    "enable.auto.offset.store": False,
    'bootstrap.servers': 'localhost:9092',
    "group.id": 'runner.group',
    'schema.registry.url': 'http://localhost:8081',
    # the consumer was not running without default.topic.config
    "default.topic.config": {"auto.offset.reset": "smallest"}
}

consumer = AvroConsumer(config)

topic = 'postgres-stocks'
consumer.subscribe([topic])

i = 1
try:
    while True:
        msg = consumer.poll(10)
        if msg is None:
            continue
        elif not msg.error():
            print('Received message: {} {}'.format(i, msg.value()))
            i = i + 1
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()