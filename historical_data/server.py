import logging
from concurrent import futures

import grpc

from data.db_factory import DbSessionFactory
from data.repository import Repository
from proto import historical_data_pb2
from proto import historical_data_pb2_grpc


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


def serve(max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    historical_data_pb2_grpc.add_HistoricalDataServicer_to_server(HistoricalData(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    DbSessionFactory.global_init()
    serve(10)
