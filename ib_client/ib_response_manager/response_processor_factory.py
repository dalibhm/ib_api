from ib_response_manager.api_client import DataApiClient
from ib_response_manager.test_response_processor import TestResponseManager


class ResponseProcessorFactory:
    def __init__(self, response_config):
        self.config = response_config

    def create(self):
        url = self.config['url']
        if url == '':
            return TestResponseManager()
        else:
            return DataApiClient(url)
