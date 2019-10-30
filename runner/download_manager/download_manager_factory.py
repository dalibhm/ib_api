from download_manager.data_download_manager import DataDownloadManager
from download_manager.download_config import DownloadConfig, DownloadConfigType
# from download_manager.populate_stock_in_exchange_manager import PopulateStockInExchangeManager


class DownloadManagerFactory:
    @staticmethod
    def create(download_config: DownloadConfig, ib_client, listing_service):
        if download_config.type == DownloadConfigType.Populate_Stock_In_Exchange:
            pass
            # return PopulateStockInExchangeManager(download_config, ib_client, listing_service)
        elif download_config.type == DownloadConfigType.Download_Stock_Data:
            return DataDownloadManager(download_config, ib_client, listing_service)