import sys

import grpc

from Services.ServiceBase import ServiceBase
from proto import request_data_pb2, request_data_pb2_grpc


class FundamentalDataService(ServiceBase):

    def __init__(self):
        super().__init__()
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = request_data_pb2_grpc.RequestDataStub(self.channel)

    def request_fundamental_data(self, contract, report_type):
        request = request_data_pb2.FundamentalDataRequest(
            contract=contract,
            reportType=report_type
        )
        try:
            _ = self.stub.RequestFundamentalData(request)
            self.logger.info('{} fundamental data request sent for {}'.format(report_type,
                                                                              contract.symbol)
                             )
            # self.logger.notice("Client received Historical data: " + str(response.message))
        except Exception as exception:
            # self.logger.error('Unable to receive {} fundamental data for {}'.format(report_type,
            #                                                                         exception)
            #                   )
            self.logger.exception('Unable to receive {} fundamental data for {}'.format(report_type,
                                                                                        contract.symbol),
                                  exc_info=sys.exc_info())
