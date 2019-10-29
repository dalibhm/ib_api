from time import sleep

from data_api import DataApiClient
from download_manager.data_download_manager import DownloadManager
from download_manager.download_config import PopulateStockExchangeConfig
from stock_parser.stock_parser import StockParser


class PopulateStockInExchangeManager(DownloadManager):
    def __init__(self, download_config: PopulateStockExchangeConfig, data_api_client: DataApiClient, ib_grpc_client):
        super().__init__(download_config, data_api_client, ib_grpc_client)

        self.exchanges = download_config.exchanges
        self.instruments = download_config.instruments

    def run_exchange(self, exchange):
        exchange_url = self.data_api_client.get_exchange_link(exchange)
        stock_parser = StockParser(exchange_url, exchange, self.data_api_client)
        stock_parser.parse_stock_web_pages()

    def run(self):
        for exchange in self.exchanges:
            self.run_exchange(exchange)
            sleep(0.1)
