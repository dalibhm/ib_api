from __future__ import print_function

import grpc

from proto import request_data_pb2, request_data_pb2_grpc
import scripts

channel = grpc.insecure_channel('localhost:50051')
stub = request_data_pb2_grpc.RequestDataStub(channel)

ib_symbol = 'SHOP'
conid = 0
currency = "USD"
contract = request_data_pb2.Contract(symbol=ib_symbol,
                                     secType="STK",
                                     exchange="SMART",
                                     primaryExchange="",
                                     currency=currency)
# sleep(10)
response = scripts.request_contract_details(stub, contract)
print(response)

for report_type in ['ReportsFinSummary',
                    'ReportsOwnership',
                    'ReportSnapshot',
                    'ReportsFinStatements',
                    'RESC',
                    'CalendarReport']:
    print('Sending {}'.format(report_type))
    r = scripts.request_fundamental_data(stub, contract, report_type)
    print(report_type, r)

