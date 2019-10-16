from __future__ import print_function

import datetime
import logging
from time import sleep

import grpc_files

from proto import request_data_pb2, request_data_pb2_grpc


def historical_data_request(stub, contract):
    queryTime = (datetime.datetime.today() - datetime.timedelta(days=30)).strftime("%Y%m%d %H:%M:%S")
    request = request_data_pb2.HistoricalDataRequest(
        contract=contract,
        endDateTime=queryTime,
        durationString="1 M",
        barSizeSetting="1 day",
        whatToShow="MIDPOINT",
        useRTH=1,
        formatDate=1,
        keepUpToDate=False)
    response = stub.RequestHistoricalData(request)
    print("Testbed client received Historical data: " + str(response.message))


def request_fundamental_data(stub, contract, report_type):
    request = request_data_pb2.FundamentalDataRequest(
        contract=contract,
        reportType=report_type
    )
    response = stub.RequestFundamentalData(request)
    print("response: {}".format(response))


def request_contract_details(stub, contract):
    request = request_data_pb2.ContractDetailsRequest(
        contract=contract
    )
    response = stub.RequestContractDetails(request)


def run():
    channel = grpc_files.insecure_channel('localhost:50051')
    stub = request_data_pb2_grpc.RequestDataStub(channel)
    contract = request_data_pb2.Contract(conId=0,
                                         symbol="SHOP",
                                         secType="STK",
                                         exchange="SMART",
                                         primaryExchange="",
                                         currency="USD")

    for report_type in ['ReportsFinSummary',
                        'ReportsOwnership',
                        'ReportSnapshot',
                        'ReportsFinStatements',
                        'RESC',
                        'CalendarReport']:
        print('Sending {}'.format(report_type))
        request_fundamental_data(stub, contract, report_type)

        sleep(1)
    # contract_details_request(stub, contract)


if __name__ == '__main__':
    logging.basicConfig()
    run()
