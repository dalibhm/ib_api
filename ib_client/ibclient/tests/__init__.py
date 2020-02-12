import csv
import os, sys

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))

from injector import inject

from ibclient.Services.request_id_generator import RequestIdGenerator
from ibclient.connection_manager.connection_manager import ConnectionManager
from ibapi.wrapper import EWrapper
from ibclient.api.ib_client import IbClient

from ibclient.proto.request_data_pb2 import HistoricalDataRequest, FundamentalDataRequest, \
    ContractRequest
from ibclient.proto.request_data_pb2 import Contract


class IdGenTest(RequestIdGenerator):
    pass


class ConnTest(ConnectionManager):
    hold_on_requests = False


class ClientTest(IbClient):
    @inject
    def __init__(self, wrapper: EWrapper):
        super().__init__(wrapper)


class WrapperTest(EWrapper):
    pass


contract = Contract()
contract.conId = 0
contract.symbol = 'MOCK'
contract.secType = 'MOCK'
contract.exchange = 'MOCK'
contract.primaryExchange = 'MOCK'
contract.currency = 'MOCK'

historical_request = HistoricalDataRequest()
historical_request.contract.conId = 0
historical_request.contract.symbol = 'MOCK'
historical_request.contract.secType = 'MOCK'
historical_request.contract.exchange = 'MOCK'
historical_request.contract.primaryExchange = 'MOCK'
historical_request.contract.currency = 'MOCK'
historical_request.endDateTime = '20191210'
historical_request.durationString = '1M'
historical_request.barSizeSetting = '1 d'
historical_request.whatToShow = 'TRADE'
historical_request.useRTH = 0
historical_request.formatDate = 1
historical_request.keepUpToDate = False


def read_stocks():
    stocks = []
    with open('stocks_amex.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # con_id = row['con_id']
            # symbol = row['symbol']
            # currency = row['currency']
            # exchange = row['exchange']
            #
            # stock = (con_id, symbol, currency, exchange)
            stocks.append(row)
    return stocks


def historical_request(stock):
    historical_request = HistoricalDataRequest()
    historical_request.contract.conId = int(stock['con_id'])
    historical_request.contract.symbol = stock['symbol']
    historical_request.contract.secType = 'STK'
    historical_request.contract.exchange = stock['exchange']
    historical_request.contract.primaryExchange = stock['exchange']
    historical_request.contract.currency = stock['currency']
    historical_request.endDateTime = '20191210 00:00:00 GMT'
    historical_request.durationString = '1 M'
    historical_request.barSizeSetting = '1 day'
    historical_request.whatToShow = 'TRADES'
    historical_request.useRTH = 0
    historical_request.formatDate = 1
    historical_request.keepUpToDate = False
    return historical_request

def fundamental_request(stock):
    f_request = FundamentalDataRequest()
    f_request.contract.conId = int(stock['con_id'])
    f_request.contract.symbol = stock['symbol']
    f_request.contract.secType = 'STK'
    f_request.contract.exchange = stock['exchange']
    f_request.contract.primaryExchange = stock['exchange']
    f_request.contract.currency = stock['currency']
    f_request.reportType = 'report.type'
    return f_request


def contract_details_request(stock):
    cdr = ContractRequest()
    cdr.contract.conId = int(stock['con_id'])
    cdr.contract.symbol = stock['symbol']
    cdr.contract.secType = 'STK'
    cdr.contract.exchange = stock['exchange']
    cdr.contract.primaryExchange = stock['exchange']
    cdr.contract.currency = stock['currency']
    return cdr