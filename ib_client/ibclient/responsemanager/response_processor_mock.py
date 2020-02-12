from ibclient.responsemanager import ResponseManager


class MockResponseManager(ResponseManager):
    def __init__(self):
        pass

    def process_contract_details(self, request, contract_details):
        print(request, contract_details)

    def process_historical_data(self, request, bar_data):
        print(request, bar_data)

    def process_fundamental_data(self, request, xml_data):
        print('TestResponseProcessor::from process_financial_data')
        print(request, xml_data)
