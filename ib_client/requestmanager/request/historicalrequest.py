import threading

from requestmanager.request.request import Request


class HistoricalRequest(Request):

    def __init__(self, request):
        super().__init__(request)
        self.lock = threading.Lock()
        self.name = "HistoricalRequest"

    # def add_data(self, data):
    #     self._data.append(data)
    #
    # # implement in inherited classes
    # def __repr__(self):
    #     return 'symbol {} started {} ended {}'.format(self.symbol, self.response_time, self.response_time)
