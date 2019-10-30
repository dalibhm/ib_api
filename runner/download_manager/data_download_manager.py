from time import sleep

from data_requests import request_factory
from data_requests.fundamental_request import FundamentalRequest
from data_requests.historical_request import HistoricalRequest
from download_manager.download_manager import DownloadManager
from request_templates.params_factory import RequestTemplateFactory
from services.listing_service import ListingService


class DataDownloadManager(DownloadManager):
    def __init__(self, download_config, ib_client, listing_service: ListingService):
        super().__init__(download_config, ib_client, listing_service)

        self.stocks = None
        self.exchanges = None
        if download_config.stocks:
            self.stocks = download_config.stocks
        else:
            self.exchanges = download_config.exchanges

        request_template_factory = RequestTemplateFactory()
        self.request_template = request_template_factory.create(download_config.data_config)

    def run(self):
        if self.stocks:
            for stock in self.stocks:
                contract = self.listing_service.get_stock_listing(stock)
                self.run_stock(contract)
                # sleep(0.1)
        else:
            for exchange in self.exchanges:
                for contract in self.listing_service.get_stocks_in_exchange(exchange):
                    self.run_stock(contract)
                    # sleep(0.1)

    def run_stock(self, contract):
        request = request_factory.create_request(contract, self.request_template)
        self.send(request)

    def send(self, request):
        if isinstance(request, FundamentalRequest):
            for report_type in request.request_template:
                self.ib_client.request_fundamental_data(request.contract, report_type)
                sleep(0.5)
        elif isinstance(request, HistoricalRequest):
            self.ib_client.request_historical_data(request.contract, request.request_template)
        else:
            raise Exception('request object is neither FundamentalRequest nor HistoricalRequest')
