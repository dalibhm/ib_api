import logging

from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.cimpl import KafkaException

from runner.exceptions import EndOfTopic, NoMessage

logger = logging.getLogger(__name__)


class KafkaConsumer:
    """
    Base class for all runners... maybe
    """

    def __init__(self, group_id, topic, default_topic_config, config=None):
        super().__init__()
        self.topic = topic

        self.kafka_config = {
            "api.version.request": True,
            "enable.auto.commit": True,
            "enable.auto.offset.store": False,
            'bootstrap.servers': config.get('kafka', 'bootstrap.servers'),
            "group.id": group_id,
            'schema.registry.url': config.get('kafka', 'schema.registry.url'),
            # the consumer was not running without default.topic.config
            "default.topic.config": default_topic_config,
            # "MaxPollIntervalMs": config.get('kafka', 'MaxPollIntervalMs'),
            # "default.topic.config": {"auto.offset.reset": "earliest"}
        }
        self.consumer = AvroConsumer(self.kafka_config)
        self.consumer.subscribe([self.topic])

    def poll(self):
        msg = self.consumer.poll(0.1)
        if msg is None:
            raise NoMessage
        elif not msg.error():
            logger.info('Received message: {}'.format(msg.value()))
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            logger.info('End of partition reached {0}/{1}'.format(msg.topic(), msg.partition()))
            raise EndOfTopic
        else:
            logger.exception('Error occured in Kafka: {0}'.format(msg.error().str()))
            raise KafkaException
        return msg.value()
