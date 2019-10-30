import grpc

from proto.ib_client import request_data_pb2, request_data_pb2_grpc


class IbClient:
    def __init__(self, server_url):
        self.logger = None
        self.channel = grpc.insecure_channel(server_url)
        self.stub = request_data_pb2_grpc.RequestDataStub(self.channel)

    def request_contract_details(self, contract):
        contract = request_data_pb2.Contract(conId=contract.conId,
                                             symbol=contract.symbol,
                                             secType=contract.secType,
                                             exchange=contract.exchange,
                                             primaryExchange=contract.primaryExchange,
                                             currency=contract.currency)
        request = request_data_pb2.ContractDetailsRequest(contract=contract)
        try:
            _ = self.stub.RequestContractDetails(request)
            self.log_success('contract details', contract.symbol)
        except Exception as e:
            self.log_failure('details details', contract.symbol)

    def request_fundamental_data(self, contract, report_type):
        request = request_data_pb2.FundamentalDataRequest(
            contract=contract,
            reportType=report_type
        )
        try:
            _ = self.stub.RequestFundamentalData(request)
            self.log_success('fundamental', contract['symbol'], report_type)
        except Exception as exception:
            self.log_failure('fundamental', contract['symbol'], report_type)

    def request_historical_data(self, contract, params):
        contract_grpc = request_data_pb2.Contract(**contract)
        request = request_data_pb2.HistoricalDataRequest(contract=contract_grpc, **params)
        try:
            _ = self.stub.RequestHistoricalData(request)
            self.log_success('historical', contract['symbol'])
        except Exception as exception:
            self.log_failure('fundamental', contract['symbol'])

    def log_success(self, request_type, symbol, report_type=None):
        pass
        # self.logger.info('{}: {} {} request sent'.format(request_type, symbol, report_type))

    def log_failure(self, request_type, symbol, report_type=None):
        pass
        # if report_type is None:
        #     self.logger.exception('{}: {} request failed'.format(request_type, symbol),
        #                           exc_info=sys.exc_info())
        # else:
        #     self.logger.exception('{}: {} {} request failed'.format(request_type, symbol, report_type),
        #                           exc_info=sys.exc_info())
