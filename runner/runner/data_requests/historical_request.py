from data_requests.request import Request


class HistoricalRequest(Request):
    def __init__(self, contract, request_template):
        Request.__init__(self, contract, request_template)