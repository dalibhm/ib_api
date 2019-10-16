from abc import ABC, abstractmethod


class ResponseProcessor(ABC):

    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def process_financial_data(self, request, xml_data):
        pass

    @abstractmethod
    def process_historical_data(self, request, bar_data):
        pass

    @abstractmethod
    def process_contract_details(self, request, contract_details):
        pass
