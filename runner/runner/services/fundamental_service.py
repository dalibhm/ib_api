import grpc
import logging
from proto.fundamental import fundamental_data_pb2, fundamental_data_pb2_grpc


class FundamentalService:
    def __init__(self, server_url):
        self.logger = None
        self.channel = grpc.insecure_channel(server_url)
        self.stub = fundamental_data_pb2_grpc.FundamentalDataStub(self.channel)

    def is_up_to_date(self, stock):
        try:
            request = fundamental_data_pb2.StockRequest(stock=stock)
            response = self.stub.IsUpToDate(request)
            return response.upToDate
        except Exception as e:
            logging.error(stock, e)
            return False
