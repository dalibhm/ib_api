from configparser import ConfigParser

import grpc
import logging

from injector import inject

from proto.historical_data import historical_data_pb2_grpc, historical_data_pb2

logger = logging.getLogger()


class HistoricalDataService:
    @inject
    def __init__(self, config: ConfigParser):
        server_url = config.get('services', 'historical_data')
        if server_url:
            self.channel = grpc.insecure_channel(server_url)
            self.stub = historical_data_pb2_grpc.HistoricalDataStub(self.channel)

    def get_latest_timestamp(self, stock, format):
        try:
            request = historical_data_pb2.Request(stock=stock, dateFormat=format)
            response = self.stub.GetLatestTimeStamp(request)
            if isinstance(response, historical_data_pb2.Result):
                return response.date
            else:
                return False
        except Exception as e:
            logger.exception('unhandled exception getting latest timestamp for {}'.format(stock))
            return False
