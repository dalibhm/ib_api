from configparser import ConfigParser

import grpc
from injector import inject

from proto.listing import listing_pb2, listing_pb2_grpc


class ListingService:
    @inject
    def __init__(self, config: ConfigParser):
        self.logger = None
        server_url = config.get('services', 'stock_listing')
        self.channel = grpc.insecure_channel(server_url)
        self.stub = listing_pb2_grpc.ListingStub(self.channel)

    def get_stocks_in_exchange(self, exchange_code):
        request = listing_pb2.ExchangeRequest(code=exchange_code)
        stream_response = self.stub.GetStocksInExchange(request)
        for response in stream_response:
            contract = {'conId': response.conId,
                        'symbol': response.symbol,
                        'secType': 'STK',
                        'exchange': response.exchange,
                        'currency': response.currency
                        }
            yield contract

    def get_stock_listing(self, stock_symbol):
        request = listing_pb2.StockRequest(symbol=stock_symbol)
        response = self.stub.GetStockListing(request)
        yield {'conId': response.conId,
               'symbol': response.symbol,
               'secType': 'STK',
               'exchange': response.exchange,
               'currency': response.currency
               }
