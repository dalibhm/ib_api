import logging
import grpc

from ib_response_manager.response_manager import ResponseManager
from requestmanager.requestmanager import RequestManager
from _external import fundamental_data_pb2_grpc
from _external import fundamental_data_pb2

logger = logging.getLogger(__name__)


class GrpcResponseManager(ResponseManager):
    def __init__(self, server_url, request_manager: RequestManager):

        self.channel = grpc.insecure_channel(server_url)
        self.stub = fundamental_data_pb2_grpc.FundamentalDataStub(self.channel)
        self.request_manager: RequestManager = request_manager

    def process_financial_data(self, request_id, xml_data):
        request = self.request_manager.get_request_by_id(request_id)['request']
        report = fundamental_data_pb2.ReportRequest(stock=request.contract.symbol,
                                                    reportType=request.reportType,
                                                    content=xml_data)
        try:
            self.stub.ProcessReport(report)
        except grpc.RpcError as e:
            logger.exception(
                'error sending data tp fundamental server {} {}'.format(request.contract.symbol, request.reportType))

    def process_historical_data(self, request, bar_data):
        pass

    def process_contract_details(self, request, contract_details):
        pass
