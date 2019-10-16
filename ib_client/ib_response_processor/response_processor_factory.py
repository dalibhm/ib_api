from ib_response_processor.api_client import DataApiClient
from ib_response_processor.test_response_processor import TestResponseProcessor


class ResponseProcessorFactory:
    def __init__(self, response_config):
        self.config = response_config

    def create(self):
        url = self.config['url']
        if url == '':
            return TestResponseProcessor()
        else:
            return DataApiClient(url)
