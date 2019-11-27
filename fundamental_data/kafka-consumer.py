from confluent_kafka import Consumer
from kafka.errors import KafkaError
import json

from mongo_documents.statement import Statement

consumer = Consumer(
    {
        "api.version.request": True,
        "enable.auto.commit": True,
        "group.id": 'group_id',
        "bootstrap.servers": 'localhost:9093,localhost:9094',
        "default.topic.config": {"auto.offset.reset": "smallest"}
    }
)

topic = 'fundamental-data'
consumer.subscribe([topic])


def save_record(binary_record):
    record = Statement(**json.loads(binary_record))
    existing_records = Statement.objects(ticker=record.ticker)
    if existing_records:
        for existing_record in existing_records:
            if record.statement.replace('\r', '') == existing_record.statement.replace('\r', ''):
                return
    record.save()



try:
    while True:
        msg = consumer.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            save_record(msg.value())
            print('Received message: {} {}'.format(msg.key().decode('utf-8'), msg.value().decode('utf-8')))
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))

except KeyboardInterrupt:
    pass

finally:
    consumer.close()