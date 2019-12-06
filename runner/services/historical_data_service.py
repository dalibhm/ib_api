import grpc
import logging
from proto.historical_data import historical_data_pb2, historical_data_pb2_grpc

logger = logging.getLogger()


class HistoricalDataService:
    def __init__(self, server_url):
        self.logger = None
        self.channel = grpc.insecure_channel(server_url)
        self.stub = historical_data_pb2_grpc.HistoricalDataStub(self.channel)

    def get_latest_timestamp(self, stock, format):
        try:
            request = historical_data_pb2.Request(stock=stock, dateFormat=format)
            response = self.stub.GetLatestTimeStamp(request)
            return response.date
        except Exception as e:
            logger.exception('unhandled exception getting latest timestamp for {}'.format(stock))
            return False
