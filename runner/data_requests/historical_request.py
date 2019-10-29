from data_requests.request import Request


class HistoricalRequest(Request):
    def __init__(self, stock, request_template, data_api_client, ib_client_grpc):
        Request.__init__(self, stock, request_template, data_api_client, ib_client_grpc)

    def send(self):
        self.get_contract()
        self.ib_grpc_client.request_historical_data(self.contract, self.request_template)
