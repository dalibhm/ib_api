import logging
from configparser import ConfigParser

import grpc
from injector import inject


from _external import fundamental_data_pb2, fundamental_data_pb2_grpc
from responsemanager.fundamental_processor import FundamentalDataProcessor

logger = logging.getLogger(__name__)


class GrpcFundamentalDataProcessor(FundamentalDataProcessor):

    @inject
    def __init__(self, config: ConfigParser):
        server_url = config.get('services', 'fundamental_data')
        self.channel = grpc.insecure_channel(server_url)
        self.stub = fundamental_data_pb2_grpc.FundamentalDataStub(self.channel)

    def process_data(self, request_id, request, xml_data):
        report = fundamental_data_pb2.Report(stock=request.contract.symbol,
                                             reportType=request.reportType,
                                             content=xml_data)
        try:
            self.stub.ProcessReport(report)
        except grpc.RpcError as e:
            logger.exception(
                'error sending data tp fundamental server {} {}'.format(request.contract.symbol,
                                                                        request.reportType))

    def process_data_end(self, request_id, request):
        pass

    def process_error(self, request_id, request, error_code, error_string):
        print(request_id, request.contract.symbol, error_code, error_string)
