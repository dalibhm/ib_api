
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
