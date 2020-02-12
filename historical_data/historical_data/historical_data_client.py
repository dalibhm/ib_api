import grpc
import logging

from .proto import historical_data_pb2, historical_data_pb2_grpc

logger = logging.getLogger()


class HistoricalDataService:
    def __init__(self, server_url):
        if server_url:
            self.channel = grpc.insecure_channel(server_url)
            self.stub = historical_data_pb2_grpc.HistoricalDataStub(self.channel)

    def get_end_db(self, symbol, date_format='%Y%m%d'):
        request = historical_data_pb2.Request(stock=symbol, dateFormat=date_format)
        response = self.stub.GetEndDb(request)
        return response.date

    def get_start_db(self, symbol, date_format='%Y%m%d'):
        request = historical_data_pb2.Request(stock=symbol, dateFormat=date_format)
        response = self.stub.GetStartDb(request)
        return response.date


if __name__ == '__main__':
    url = '127.0.0.1:12599'
    service = HistoricalDataService(url)
