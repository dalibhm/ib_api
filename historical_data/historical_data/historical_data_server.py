import logging
import os
import time
from concurrent import futures
from configparser import ConfigParser

import grpc

from data.repository import Repository
from proto import historical_data_pb2, historical_data_pb2_grpc

if not os.path.exists("../log"):
    os.makedirs("../log")

FORMAT = '%(asctime)-15s %(levelname)s %(name)-s %(message)s'

logging.basicConfig(filename=time.strftime(os.path.join("../log", "historical_data_%Y%m%d_%H_%M_%S.log")),
                    filemode="w",
                    level=logging.DEBUG,
                    format=FORMAT)
logger = logging.getLogger()


class HistoricalData(historical_data_pb2_grpc.HistoricalDataServicer):

    def GetOneHistoricalData(self, request, context):
        historical_data = Repository.get_historical_data_for_stock(request.stock,
                                                                   request.startDate,
                                                                   request.endDate,
                                                                   request.priceType)
        for data in historical_data:
            yield data.to_proto()

    def GetManyHistoricalData(self, request_iterator, context):
        for request in request_iterator:
            historical_data = Repository.get_historical_data_for_stock(request.stock,
                                                                       request.startDate,
                                                                       request.endDate,
                                                                       request.priceType)
            for data in historical_data:
                yield historical_data_pb2.BarData(data.to_proto())

    def AddHistoricalData(self, request, context):
        pass

    def GetHeadTimeStamp(self, request, context):
        pass

    def GetStartDb(self, request, context):
        try:
            stock = request.stock
            price_type = request.priceType
            date_format = request.dateFormat
            date = Repository.get_start_db(stock, date_format)
            # result = historical_data_pb2.Timestamp(date)
            if date:
                return historical_data_pb2.Result(date=date)
            else:
                return historical_data_pb2.Empty()
        except:
            logger.exception('unhandled exception in GetLatestTimeStamp for {}'.format(stock))
            return historical_data_pb2.Empty()

    def GetEndDb(self, request, context):
        try:
            stock = request.stock
            price_type = request.priceType
            date_format = request.dateFormat
            date = Repository.get_end_db(stock, date_format)
            # result = historical_data_pb2.Timestamp(date)
            if date:
                return historical_data_pb2.Result(date=date)
            else:
                return historical_data_pb2.Empty()
        except:
            logger.exception('unhandled exception in GetLatestTimeStamp for {}'.format(stock))
            return historical_data_pb2.Empty()


def serve(endpoint, max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    historical_data_pb2_grpc.add_HistoricalDataServicer_to_server(HistoricalData(), server)
    server.add_insecure_port(endpoint)
    server.start()
    logger.info('Listing server started...')
    logger.info('Listening on {}'.format(endpoint))
    server.wait_for_termination()


def main():
    environment = os.getenv('environment') or 'development'

    config = ConfigParser()
    config.read(os.path.join('../settings', environment + '.ini'))
    endpoint = config.get('services', 'historical_data')

    # initialize database
    # DbSessionFactory.global_init()
    Repository.init(config)
    serve(endpoint, 10)


if __name__ == '__main__':
    main()
