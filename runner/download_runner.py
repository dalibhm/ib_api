from download_manager.download_config import DownloadConfigFactory
from download_manager.download_manager_factory import DownloadManagerFactory
from request_templates.params_factory import RequestTemplateFactory


class DownloadRunner:
    def __init__(self, download_config, services):
        self.services = services
        self.download_config = download_config

    def go(self):
        for download_config in self.download_config.values():
            download_config_template = DownloadConfigFactory.create(download_config)
            download_manager_gen = DownloadManagerFactory.create(download_config_template,
                                                                 self.services)
        for download_manager in download_manager_gen:
            download_manager.run()
