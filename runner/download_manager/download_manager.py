from data_requests.request_factory import RequestFactory


class DownloadManager:
    def __init__(self, download_config, data_api_client, ib_grpc_client):
        self.download_config = download_config
        self.data_api_client = data_api_client
        self.request_factory = RequestFactory(data_api_client, ib_grpc_client)