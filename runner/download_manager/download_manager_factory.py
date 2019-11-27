from download_manager.download_manager import DownloadManager
from download_manager.download_config import DownloadConfig, DownloadConfigType
# from download_manager.populate_stock_in_exchange_manager import PopulateStockInExchangeManager
from request_templates.params_factory import RequestTemplateFactory


class DownloadManagerFactory:
    @staticmethod
    def create(download_config: DownloadConfig, services):
        request_template_factory = RequestTemplateFactory()
        request_template = request_template_factory.create(download_config.data_config)
        if download_config.type == DownloadConfigType.Populate_Stock_In_Exchange:
            pass
            # return PopulateStockInExchangeManager(download_config, ib_client, listing_service)
        elif download_config.type == DownloadConfigType.Download_Stock_Data:
            if download_config.stocks:
                for stock in download_config.stocks:
                    contract = services['listing'].get_stock_listing(stock)
                    yield DownloadManager(contract, request_template, services)
            else:
                for exchange in download_config.exchanges:
                    for contract in services['listing'].get_stocks_in_exchange(exchange):
                        yield DownloadManager(contract, request_template, services)