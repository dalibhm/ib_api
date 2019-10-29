from time import sleep

from data_requests.request import Request
from services.ib_client import IbClient


class FundamentalRequest(Request):
    def __init__(self, stock, request_template, data_api_client, ib_client_grpc: IbClient):
        Request.__init__(self, stock, request_template, data_api_client, ib_client_grpc)

    def send(self):
        self.get_contract()
        for report_type in self.request_template:
            self.ib_grpc_client.request_fundamental_data(self.contract, report_type)
            sleep(0.1)
