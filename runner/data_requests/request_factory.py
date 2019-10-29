from request_templates.params import RequestTemplate
from data_requests.historical_request import HistoricalRequest
from data_requests.fundamental_request import FundamentalRequest
from custom_types.request_type import RequestType


class RequestFactory:
    def __init__(self, data_api_client, ib_client):
        self.data_api_client = data_api_client
        self.ib_client = ib_client

    def create(self, stock, request_template: RequestTemplate):
        if request_template.type == RequestType.Historical:
            return HistoricalRequest(stock, request_template.params, self.data_api_client, self.ib_client)
        elif request_template.type == RequestType.Fundamental:
            return FundamentalRequest(stock, request_template.params, self.data_api_client, self.ib_client)