from abc import ABC, abstractmethod


class HistoricalDataProcessor(ABC):

    @abstractmethod
    def process_data(self, request_id, request, bar_data):
        pass

    @abstractmethod
    def process_data_end(self, request_id, request, start, end):
        pass

    @abstractmethod
    def process_error(self, request_id, request, error_code, error_string):
        pass