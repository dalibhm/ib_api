import sys

import grpc

from Services.ServiceBase import ServiceBase
from proto import request_data_pb2, request_data_pb2_grpc


class HistoricalDataService(ServiceBase):

    def __init__(self):
        super().__init__()
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = request_data_pb2_grpc.RequestDataStub(self.channel)

    def request_historical_data(self, contract, end_date_time, historical_data_length='1 Y',
                                bar_size='1 day', price_type='ADJUSTED_LAST'):
        _end_date_time = end_date_time.strftime("%Y%m%d %H:%M:%S")
        request = request_data_pb2.HistoricalDataRequest(
            contract=contract,
            endDateTime=_end_date_time,
            durationString=historical_data_length,
            barSizeSetting=bar_size,
            whatToShow=price_type,
            useRTH=1,
            formatDate=1,
            keepUpToDate=False)
        try:
            _ = self.stub.RequestHistoricalData(request)
            self.logger.info('Historical data request sent for {}'.format(contract.symbol))
            # self.logger.info("Client received Historical data: " + str(response.message))
        except Exception as exception:
            # self.logger.error('Unable to request historical data for {}'.format(contract.symbol))
            self.logger.exception('Unable to request historical data for {}'.format(contract.symbol),
                                  exc_info=sys.exc_info())

