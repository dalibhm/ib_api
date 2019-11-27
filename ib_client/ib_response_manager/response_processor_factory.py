from ib_response_manager.api_client import DataApiClient
from ib_response_manager.kafka.kafka_response_processor import KafkaResponseManager


class ResponseProcessorFactory:
    def __init__(self, config):
        self.config = config

    def create(self, request_manager):
        url = self.config.get('data api', 'data_api_server')
        if url == '':
            return KafkaResponseManager(self.config, request_manager)
        else:
            return DataApiClient(url)
