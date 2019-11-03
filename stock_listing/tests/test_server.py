import grpc
from pytest import fixture


import stock_listing.proto.listing_pb2_grpc as listing_pb2_grpc
import stock_listing.proto.listing_pb2 as listing_pb2

@fixture
def start_server():
    pass


@fixture
def connection():
    channel = grpc.insecure_channel('[::]:12499')
    yield listing_pb2_grpc.ListingStub(channel)
    channel.close()


def test_listing_service_call(connection):
    request = listing_pb2.ExchangeRequest(code='nyse')
    stream_response = connection.GetStocksInExchange(request)
    for response in stream_response:
        contract = {'conId': response.conId,
                    'symbol': response.symbol,
                    'secType': 'STK',
                    'exchange': response.exchange,
                    'currency': response.currency
                    }
        assert contract['exchange'] == 'nyse'
