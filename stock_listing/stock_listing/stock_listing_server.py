from concurrent import futures
from configparser import ConfigParser

import grpc

from logbook import Logger
from container import Container
from injector import inject, Injector

from logger import LogService
from proto import listing_pb2_grpc
from data.repository import Repository


class Listing(listing_pb2_grpc.ListingServicer):
    def __init__(self, repository: Repository, logger: Logger):
        self.repository = repository
        self.logger = logger

    def GetStockListing(self, request, context):
        try:
            self.logger.notice('Request for stock {}'.format(request.symbol))
            response = self.repository.get_stock_by_symbol(request.symbol)
            return response.get_stock_listing()
        except:
            self.logger.exception('Request for stock {}'.format(request.symbol))

    def GetStocksInExchange(self, request, context):
        try:
            self.logger.notice('Request for exchange {}'.format(request.code))
            exchange_code = request.code
            stocks = self.repository.get_stocks_in_exchange(exchange_code)
            for stock in stocks:
                yield stock.get_stock_listing()
        except:
            self.logger.exception('Request for exchange {}'.format(request.code))


def serve(endpoint, max_workers, repository, logger: Logger):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    listing_service = Listing(repository=repository, logger=logger)
    listing_pb2_grpc.add_ListingServicer_to_server(listing_service, server)
    server.add_insecure_port('0.0.0.0:12499')
    server.add_insecure_port(endpoint)
    server.start()
    logger.notice('Listening on {}'.format(endpoint))

    server.wait_for_termination()


if __name__ == '__main__':
    # container = Container()
    injector = Injector([Container])
    config = injector.get(ConfigParser)
    endpoint = config.get('services', 'stock_listing')
    repository = injector.get(Repository)
    logger = injector.get(LogService).get_startup_log()
    serve(endpoint, 10, repository, logger)
