from request_templates.params import RequestTemplate
from data_requests.historical_request import HistoricalRequest
from data_requests.fundamental_request import FundamentalRequest
from custom_types.request_type import RequestType


def create_request(contract, request_template: RequestTemplate):
    if request_template.type == RequestType.Historical:
        return HistoricalRequest(contract, request_template.params)
    elif request_template.type == RequestType.Fundamental:
        return FundamentalRequest(contract, request_template.params)