import logging
from concurrent import futures

import grpc

from data.db_factory import DbSessionFactory
from proto import listing_pb2_grpc
from data.repository import Repository


class Listing(listing_pb2_grpc.ListingServicer):
    def __init__(self):
        pass

    def GetStockListing(self, request, context):
        response = Repository.get_stock_by_symbol(request.symbol)
        return response.get_stock_listing()

    def GetStocksInExchange(self, request, context):
        exchange_code = request.code
        stocks = Repository.get_stocks_in_exchange(exchange_code)
        for stock in stocks:
            yield stock.get_stock_listing()


def serve(max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    listing_pb2_grpc.add_ListingServicer_to_server(Listing(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print('Listing server started...')
    server.wait_for_termination()


if __name__ == '__main__':
    DbSessionFactory.global_init()
    logging.basicConfig()
    serve(10)
