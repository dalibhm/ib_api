from data_api import DataApiClient
from services.ib_client import IbClient


class Request:
    def __init__(self, stock, request_template, data_api_client: DataApiClient, ib_grpc_client: IbClient):
        self.stock = stock
        self.request_template = request_template
        self.data_api_client = data_api_client
        self.ib_grpc_client = ib_grpc_client
        self.contract = None

    def get_contract(self):
        stock_listing = self.data_api_client.get_stock_listing(self.stock)
        # self.contract = self.data_api_client.get_contract(con_id)
        self.contract = {'conId': stock_listing['con_id'],
                         'symbol': stock_listing['ib_symbol'],
                         'secType': 'STK',
                         'exchange': stock_listing['exchange'],
                         'primaryExchange': stock_listing['exchange'],
                         'currency': stock_listing['currency']}

    def send(self):
        pass
