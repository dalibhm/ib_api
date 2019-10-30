from ib_response_manager.api_client import DataApiClient
from ib_response_manager.test_response_processor import TestResponseManager


class ResponseProcessorFactory:
    def __init__(self, config):
        self.config = config

    def create(self):
        url = self.config.get('data api', 'data_api_server')
        if url == '':
            return TestResponseManager()
        else:
            return DataApiClient(url)
