# from confluent_kafka import avro
from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer

from data import db_factory
from data.repository import Repository

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

topic = 'historical-data'
consumer.subscribe([topic])

db_factory.DbSessionFactory.global_init()

i = 1
try:
    while True:
        msg = consumer.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print('Received message: {} {}'.format(i, msg.value()))
            try:
                Repository.add_historical_data(msg.value())
            except Exception as e:
                print(e)

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