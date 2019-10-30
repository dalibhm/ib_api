from download_manager.data_download_manager import DataDownloadManager
from download_manager.download_config import DownloadConfigFactory
from download_manager.download_manager_factory import DownloadManagerFactory
from request_templates.params_factory import RequestTemplateFactory


class DownloadRunner:
    def __init__(self, download_config, ib_client, listing_service):
        self.download_config = download_config
        self.listing_service = listing_service
        self.ib_client = ib_client

    def go(self):
        for download_config in self.download_config.values():
            download_config_template = DownloadConfigFactory.create(download_config)
            download_manager = DownloadManagerFactory.create(download_config_template, self.ib_client, self.listing_service)
            download_manager.run()



