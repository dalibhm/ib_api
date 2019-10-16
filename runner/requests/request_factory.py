class RequestFactory:
    def __init__(self):
        pass

    def create(self, stock, request_type):
        if request_type == 'historical':
            return HistoricalRequest(stock, request_type)
        elif request_type == 'fundamental':
            return FundamentalRequest(....)