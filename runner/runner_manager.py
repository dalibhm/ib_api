from time import sleep

import requests

from runner.requests.request_factory import RequestFactory


class RunnerManager:
    def __init__(self, data_config, data_api_url):
        self.stocks = data_config['stocks']
        self.data = data_config['data']
        self.data_api_url = data_api_url
        self.request_factory = RequestFactory()
        self.requests = []

    def create_requests(self):
        for stock in self.stocks:
            for request_type in self.data:
                request = self.request_factory(stock, request_type, request_params)
                self.requests.append(request)

    def send_requests(self):
        for request in self.requests:
            request.send()
            sleep(1)



