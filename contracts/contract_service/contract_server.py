import logging
import os
import time
from concurrent import futures
from configparser import ConfigParser

import grpc

from data.contract_details import ContractDetails
from data.contract import Contract
from data.repository import Repository
from proto import contract_pb2
from proto import contract_pb2_grpc

if not os.path.exists("../log"):
    os.makedirs("../log")

FORMAT = '%(asctime)-15s %(levelname)s %(name)-s %(message)s'

logging.basicConfig(filename=time.strftime(os.path.join("../log", "contract_details_%Y%m%d_%H_%M_%S.log")),
                    filemode="w",
                    level=logging.DEBUG,
                    format=FORMAT)
logger = logging.getLogger()


class ContractService(contract_pb2_grpc.ContractServiceServicer):

    def AddContract(self, request: contract_pb2.Contract, context):
        contract = Contract.from_proto(request)
        con_id = contract.conId
        symbol = contract.symbol
        Repository.add_contract(contract)
        logger.info('added contract details for {} {}'.format(con_id, symbol))
        return contract_pb2.Empty()

    def GetContract(self, request: contract_pb2.Request, context):
        data = Repository.get_contract(request.conId)
        return data.to_proto()

    def AddContractDetails(self, request: contract_pb2.ContractDetails, context):
        contract_details = ContractDetails.from_proto(request)
        contract_id = contract_details.contractId
        Repository.add_contract_details(contract_details)
        logger.info('added contract details for {}'.format(contract_id))
        return contract_pb2.Empty()

    def GetContractDetails(self, request: contract_pb2.Request, context):
        data = Repository.get_contract_details(request.conId)
        return data.to_proto()


def serve(endpoint, max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    contract_pb2_grpc.add_ContractServiceServicer_to_server(ContractService(), server)
    # server.add_insecure_port(endpoint)
    server.add_insecure_port('0.0.0.0:12422')
    server.start()
    logger.info('Listing server started...')
    logger.info('Listening on {}'.format(endpoint))
    server.wait_for_termination()


def main():
    environment = os.getenv('environment') or 'development'

    config = ConfigParser()
    config.read(os.path.join('../settings', environment + '.ini'))
    endpoint = config.get('services', 'contract_details')

    # initialize database
    # DbSessionFactory.global_init()
    Repository.init(config)
    serve(endpoint, 10)


if __name__ == '__main__':
    main()
