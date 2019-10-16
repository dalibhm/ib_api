from ib_response_processor.response_processor import ResponseProcessor


class TestResponseProcessor(ResponseProcessor):
    def __init__(self):
        pass

    def process_contract_details(self, request, contract_details):
        print(request, contract_details)

    def process_historical_data(self, request, bar_data):
        print(request, bar_data)

    def process_financial_data(self, request, xml_data):
        print('TestResponseProcessor::from process_financial_data')
        print(request, xml_data)
