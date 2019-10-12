import abc
from datetime import datetime


class Response(abc.ABC):
    def __init__(self):
        self.response_time = datetime.now()
        self._data = None

    @property
    def data(self):
        return self._data

    @abc.abstractmethod
    def append_data(self, request_id, data):
        """ Appends data as it is received"""


class HistoricalResponse(Response):
    def __init__(self, data):
        self._data = [data]

    def append_data(self, data):
        self._data.append(data)
        self.response_time = datetime.now()


class FundamentalResponse(Response):
    def __init__(self, data):
        self._data = data
        self.response_time = datetime.now()

    def append_data(self, data):
        NotImplementedError
