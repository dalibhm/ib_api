from __future__ import print_function

import datetime
import time
from time import sleep

import __init__
from Services.FundamentalDataService import FundamentalDataService

from sql_data.db_factory import DbSessionFactory
from sql_data.Contract import Contract as ContractDB


from proto import request_data_pb2


fundamental_data_service = FundamentalDataService()

session = DbSessionFactory.create_session()
results = session.query(ContractDB).filter(ContractDB.symbol=='CRTO')
session.close()
for res in results:
    contract = request_data_pb2.Contract(conId=res.conId,
                                         symbol=res.symbol,
                                         secType="STK",
                                         exchange=res.exchange,
                                         primaryExchange="",
                                         currency=res.currency)
    for report_type in ['ReportsFinSummary',
                        'ReportsOwnership',
                        'ReportSnapshot',
                        'ReportsFinStatements',
                        'RESC',
                        'CalendarReport']:
        print('Sending {}'.format(report_type))
        r = fundamental_data_service.request_fundamental_data(contract, report_type)
        time.sleep(1)
    time.sleep(1)

