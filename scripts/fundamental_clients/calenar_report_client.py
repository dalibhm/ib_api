from __future__ import print_function
import scripts.__init__
import time
from Services.FundamentalDataService import FundamentalDataService

from sql_data.db_factory import DbSessionFactory
from sql_data.Contract import Contract

from proto.request_data_pb2 import Contract as ContractProto

fundamental_data_service = FundamentalDataService()

session = DbSessionFactory.create_session()
results = session.query(Contract).filter(Contract.primaryExchange == "NYSE")
session.close()
for res in results:
    contract = ContractProto(conId=res.conId,
                             symbol=res.symbol,
                             secType="STK",
                             exchange=res.exchange,
                             primaryExchange="",
                             currency=res.currency)

    r = fundamental_data_service.request_fundamental_data(contract, 'CalendarReport')
    time.sleep(0.5)
