
class DownloadManager:
    def __init__(self, download_config, ib_client, listing_service):
        self.download_config = download_config
        self.listing_service = listing_service
        self.ib_client = ib_client
