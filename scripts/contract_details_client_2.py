from __future__ import print_function
import requests

import time
from services.contract_service import ContractService
from proto import request_data_pb2

contract_service = ContractService()

DATA_API_URL = 'http://localhost:5000'

r = requests.get('{}/stocks'.format(DATA_API_URL))
if r:
    print(r.status_code)


# for stock in imported_stocks:
#     print('{} - {} - {}'.format(stock.con_id, stock.ib_symbol, stock.currency))
#     contract = request_data_pb2.Contract(conId=stock.con_id,
#                                          symbol=stock.ib_symbol,
#                                          secType="STK",
#                                          exchange="",
#                                          primaryExchange="",
#                                          currency=stock.currency)
#
#     contract_service.contract_details(contract)
#
#     time.sleep(0.1)
