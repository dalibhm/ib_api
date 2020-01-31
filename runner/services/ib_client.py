import sys
from configparser import ConfigParser

import grpc

import logging

from injector import inject

from proto.ib_client import request_data_pb2, request_data_pb2_grpc


class IbClient:
    @inject
    def __init__(self, config: ConfigParser):
        self.logger = logging.getLogger(__name__)
        server_url = config.get('services', 'ib')
        self.channel = grpc.insecure_channel(server_url)
        self.stub = request_data_pb2_grpc.RequestDataStub(self.channel)

    def request_contract_details(self, contract):
        contract_grpc = request_data_pb2.Contract(**contract)
        request = request_data_pb2.ContractRequest(contract=contract_grpc)
        try:
            status = self.stub.RequestContractDetails(request)
            self.log_success('contract details', contract['symbol'])
        except Exception as e:
            self.log_failure('details details', contract['symbol'])

    def request_fundamental_data(self, contract, report_type):
        contract_grpc = request_data_pb2.Contract(**contract)
        request = request_data_pb2.FundamentalDataRequest(
            contract=contract_grpc,
            reportType=report_type
        )
        try:
            _ = self.stub.RequestFundamentalData(request)
            self.log_success('fundamental', contract['symbol'], report_type)
        except Exception as e:
            self.log_failure('fundamental', contract['symbol'], e.debug_error_string(), report_type)

    def request_historical_data(self, contract, params):
        contract_grpc = request_data_pb2.Contract(**contract)
        request = request_data_pb2.HistoricalDataRequest(contract=contract_grpc, **params)
        # try:
        status = self.stub.RequestHistoricalData(request)
        self.log_success('historical', contract['symbol'])
        return status.message
        # except Exception as e:
        #     self.log_failure('historical', contract['symbol'])
        #     return False

    def log_success(self, request_type, symbol, report_type=None):
        pass
        # self.logger.info('{}: {} {} request sent'.format(request_type, symbol, report_type))

    def log_failure(self, request_type, symbol, error_string, report_type=None):
        if report_type is None:
            self.logger.error('{}: {} request failed'.format(request_type, symbol), error_string)
        else:
            self.logger.error('{}: {} {} request failed: {}'.format(request_type, symbol, report_type, error_string))
