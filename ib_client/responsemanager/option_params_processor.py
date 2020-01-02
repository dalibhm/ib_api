from abc import ABC, abstractmethod

from ibapi.common import SetOfString, SetOfFloat


class OptionParamsProcessor(ABC):
    @abstractmethod
    def process_data(self, request_id, request, exchange: str,
                     underlyingConId: int, tradingClass: str, multiplier: str,
                     expirations: SetOfString, strikes: SetOfFloat):
        pass

    @abstractmethod
    def process_data_end(self, request_id, request):
        pass

    @abstractmethod
    def process_error(self, request_id, request, error_code, error_string):
        pass
