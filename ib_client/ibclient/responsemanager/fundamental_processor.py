from abc import ABC, abstractmethod


class FundamentalDataProcessor(ABC):
    @abstractmethod
    def process_data(self, request_id, request, xml_data):
        pass

    @abstractmethod
    def process_data_end(self, request_id, request):
        pass

    @abstractmethod
    def process_error(self, request_id, request, error_code, error_string):
        pass
