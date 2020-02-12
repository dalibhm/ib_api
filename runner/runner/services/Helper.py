from ibapi import Contract, ContractDetails

import sql_data.ContractDetails as ContractDetails_db

from runner.proto.ib_client import request_data_pb2


def contract2grpc(contract: Contract):
    return request_data_pb2.Contract(conId=contract.conId,
                                     symbol=contract.symbol,
                                     secType=contract.secType,
                                     exchange=contract.exchange,
                                     primaryExchange=contract.primaryExchange,
                                     currency=contract.currency)

def get_db_contract_details(contract_details: ContractDetails):
    db_contrct_details = ContractDetails_db.ContractDetails()

