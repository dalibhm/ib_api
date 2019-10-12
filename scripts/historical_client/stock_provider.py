from mongodb.mongo_setup import global_init
from proto import request_data_pb2
from sql_data.db_factory import DbSessionFactory
from sql_data.Contract import Contract as ContractDB

global_init()  #mongodb init

def get_contracts():
    session = DbSessionFactory.create_session()
    results = session.query(ContractDB).filter(ContractDB.symbol=='PAYC')
    session.close()

    contracts = []
    for res in results:
        contract = request_data_pb2.Contract(conId=res.conId,
                                             symbol=res.symbol,
                                             secType="STK",
                                             exchange="SMART",
                                             primaryExchange=res.primaryExchange,
                                             currency=res.currency)
        contracts.append(contract)
    return contracts
