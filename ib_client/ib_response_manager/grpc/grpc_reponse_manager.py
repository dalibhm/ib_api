import logging
import grpc

from ib_response_manager.response_manager import ResponseManager
from .proto import fundamental_data_pb2_grpc
from .proto import fundamental_data_pb2

logger = logging.getLogger(__name__)


class GrpcResponseManager(ResponseManager):
    def __init__(self, server_url):

        self.channel = grpc.insecure_channel(server_url)
        self.stub = fundamental_data_pb2_grpc.FundamentalDataStub(self.channel)

    def process_financial_data(self, request, xml_data):
        report = fundamental_data_pb2.ReportRequest(stock=request.contract.symbol,
                                                    reportType=request.reportType,
                                                    content=xml_data)
        try:
            self.stub.ProcessReport(report)
        except grpc.RpcError as e:
            logger.exception(
                'error in processing fundamental data {} {}'.format(request.contract.symbol, request.reportType))

    def process_historical_data(self, request, bar_data):
        pass

    def process_contract_details(self, request, contract_details):
        pass
