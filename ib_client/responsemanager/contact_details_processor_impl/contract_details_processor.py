from responsemanager.contract_details_processor import ContractDetailsProcessor


class ContractDetailsProcessorImpl(ContractDetailsProcessor):

    def process_data(self, request_id, request, contract_details):
        print(request_id, contract_details)

    def process_data_end(self, request_id, request):
        print(request_id)

    def process_error(self, request_id, request, error_code, error_string):
        print(request_id, error_code, error_string)
