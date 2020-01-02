import logging
import os
import time
from concurrent import futures
from configparser import ConfigParser

import grpc

# from data.db_factory import DbSessionFactory
from data.contract_details import ContractDetails
from data.repository import Repository
from proto import contract_details_pb2
from proto import contract_details_pb2_grpc

if not os.path.exists("log"):
    os.makedirs("log")

FORMAT = '%(asctime)-15s %(levelname)s %(name)-s %(message)s'

logging.basicConfig(filename=time.strftime(os.path.join("log", "option_params_%Y%m%d_%H_%M_%S.log")),
                    filemode="w",
                    level=logging.DEBUG,
                    format=FORMAT)
logger = logging.getLogger()


class ContractDetailsService(contract_details_pb2_grpc.ContractDetailsServiceServicer):

    def AddContractDetails(self, request: contract_details_pb2.ContractDetails, context):
        Repository.add_contract_details(ContractDetails.from_proto(request))
        return contract_details_pb2.Empty()

    def GetContractDetails(self, request, context):
        data = Repository.get_contractDetails(ContractDetails.from_proto(request))
        return data.to_proto()


def serve(endpoint, max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    contract_details_pb2_grpc.add_ContractDetailsServiceServicer_to_server(ContractDetailsService(), server)
    server.add_insecure_port(endpoint)
    server.start()
    logger.info('Listing server started...')
    logger.info('Listening on {}'.format(endpoint))
    server.wait_for_termination()


def main():
    environment = os.getenv('environment') or 'development'

    config = ConfigParser()
    config.read(os.path.join('settings', environment + '.ini'))
    endpoint = config.get('services', 'contract_details')

    # initialize database
    # DbSessionFactory.global_init()
    Repository.init(config)
    serve(endpoint, 10)


if __name__ == '__main__':
    main()
