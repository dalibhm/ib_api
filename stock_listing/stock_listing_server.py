import logging
import os
from concurrent import futures
from configparser import ConfigParser

import grpc

from container import Container
from injector import inject
from proto import listing_pb2_grpc
from data.repository import Repository


class Listing(listing_pb2_grpc.ListingServicer):
    @inject
    def __init__(self, repository: Repository):
        self.repository = repository

    def GetStockListing(self, request, context):
        response = self.repository.get_stock_by_symbol(request.symbol)
        return response.get_stock_listing()

    def GetStocksInExchange(self, request, context):
        exchange_code = request.code
        stocks = self.repository.get_stocks_in_exchange(exchange_code)
        for stock in stocks:
            yield stock.get_stock_listing()


def serve(endpoint, max_workers, repository):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    listing_service = Listing(repository=repository)
    listing_pb2_grpc.add_ListingServicer_to_server(listing_service, server)
    server.add_insecure_port(endpoint)
    server.start()
    print('Listing server started...')
    print('Listening on {}'.format(endpoint))

    server.wait_for_termination()


if __name__ == '__main__':
    container = Container()

    config = container.injector.get(ConfigParser)
    endpoint = config.get('services', 'stock_listing')
    repository = container.injector.get(Repository)
    logging.basicConfig()
    serve(endpoint, 10, repository)
