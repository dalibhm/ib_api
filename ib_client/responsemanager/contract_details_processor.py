from abc import abstractmethod


class ContractDetailsProcessor(object):
    @abstractmethod
    def process_data(self, request_id, request, contract_details):
        pass

    @abstractmethod
    def process_data_end(self, request_id, request):
        pass

    @abstractmethod
    def process_error(self, request_id, request, error_code, error_string):
        pass
