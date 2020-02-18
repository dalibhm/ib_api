import logging
import os
import time
from concurrent import futures
from configparser import ConfigParser

import grpc
from logger import Logger
from logger.Logger import LogService

from data.contract_details import ContractDetails
from data.contract import Contract
from data.repository import Repository
from proto import contract_pb2
from proto import contract_pb2_grpc


class ContractService(contract_pb2_grpc.ContractServiceServicer):
    def __init__(self, logger):
        self.logger = logger

    def AddContract(self, request: contract_pb2.Contract, context):
        contract = Contract.from_proto(request)
        con_id = contract.conId
        symbol = contract.symbol
        self.logger.info('adding contract details for {} {}'.format(con_id, symbol))
        Repository.add_contract(contract)
        self.logger.info('added contract details for {} {}'.format(con_id, symbol))
        return contract_pb2.Empty()

    def GetContract(self, request: contract_pb2.Request, context):
        self.logger.info('getting contract {}'.format(request.conId))
        try:
            data = Repository.get_contract(request.conId)
            if data:
                return data.to_proto()
            else:
                return contract_pb2.Contract()
        except:
            self.logger.exception('getting contract {}'.format(request.conId))

    def AddContractDetails(self, request: contract_pb2.ContractDetails, context):
        contract_details = ContractDetails.from_proto(request)
        contract_id = contract_details.contractId
        Repository.add_contract_details(contract_details)
        self.logger.info('added contract details for {}'.format(contract_id))
        return contract_pb2.Empty()

    def GetContractDetails(self, request: contract_pb2.Request, context):
        self.logger.info('getting contract details {}'.format(request.conId))
        try:
            data = Repository.get_contract_details(request.conId)
            if data:
                return data.to_proto()
            else:
                return contract_pb2.ContractDetails()
        except:
            self.logger.exception('getting contract details {}'.format(request.conId))


def serve(endpoint, max_workers, logger):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    contract_pb2_grpc.add_ContractServiceServicer_to_server(ContractService(logger), server)
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
    log_level = config.get('logging', 'log_level')
    log_location = config.get('logging', 'log_location')
    logger = LogService(log_location=log_location, filename='contract_server', log_level=log_level).Logger(
        __name__)
    serve(endpoint, 10, logger)


if __name__ == '__main__':
    main()
