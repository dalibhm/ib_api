from time import sleep

from download_manager.download_manager import DownloadManager
from request_templates.params_factory import RequestTemplateFactory


class DataDownloadManager(DownloadManager):
    def __init__(self, download_config, data_api_client, ib_grpc_client):
        super().__init__(download_config, data_api_client, ib_grpc_client)

        self.stocks = download_config.stocks
        request_template_factory = RequestTemplateFactory()
        self.request_template = request_template_factory.create(download_config.data_config)

    def run_stock(self, stock):
        request = self.request_factory.create(stock, self.request_template)
        request.send()

    def run(self):
        for stock in self.stocks:
            self.run_stock(stock)
            sleep(0.1)
