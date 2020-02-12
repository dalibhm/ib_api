from time import sleep

from data_requests.request import Request
from services.ib_client import IbClient


class FundamentalRequest(Request):
    def __init__(self, contract, request_template):
        Request.__init__(self, contract, request_template)

