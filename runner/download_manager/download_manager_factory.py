from download_manager.data_download_manager import DataDownloadManager
from download_manager.download_config import DownloadConfig, DownloadConfigType
from download_manager.populate_stock_in_exchange_manager import PopulateStockInExchangeManager


class DownloadManagerFactory:
    @staticmethod
    def create(download_config: DownloadConfig, data_api_client, ib_grpc_client):
        if download_config.type == DownloadConfigType.Populate_Stock_In_Exchange:
            return PopulateStockInExchangeManager(download_config, data_api_client, ib_grpc_client)
        elif download_config.type == DownloadConfigType.Download_Stock_Data:
            return DataDownloadManager(download_config, data_api_client, ib_grpc_client)