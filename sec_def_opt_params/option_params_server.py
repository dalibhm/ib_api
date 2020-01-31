import logging
import os
import time
from concurrent import futures
from configparser import ConfigParser

import grpc

# from data.db_factory import DbSessionFactory
from data.option_params import OptionParams
from data.repository import Repository
from proto import option_params_pb2
from proto import option_params_pb2_grpc

if not os.path.exists("log"):
    os.makedirs("log")

FORMAT = '%(asctime)-15s %(levelname)s %(name)-s %(message)s'

logging.basicConfig(filename=time.strftime(os.path.join("log", "option_params_%Y%m%d_%H_%M_%S.log")),
                    filemode="w",
                    level=logging.DEBUG,
                    format=FORMAT)
logger = logging.getLogger()


class OptionParamsService(option_params_pb2_grpc.OptionParamsServiceServicer):

    def AddRecord(self, request: option_params_pb2.OptionParams, context):
        Repository.add_option_params(OptionParams.from_proto(request))
        return option_params_pb2.Empty()

    def GetRecord(self, request, context):
        data = Repository.get_option_params(OptionParams.from_proto(request))
        return data.to_proto()


def serve(endpoint, max_workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    option_params_pb2_grpc.add_OptionParamsServiceServicer_to_server(OptionParamsService(), server)
    server.add_insecure_port(endpoint)
    server.start()
    logger.info('Listing server started...')
    logger.info('Listening on {}'.format(endpoint))
    server.wait_for_termination()


def main():
    environment = os.getenv('environment') or 'development'

    config = ConfigParser()
    config.read(os.path.join('settings', environment + '.ini'))
    endpoint = config.get('services', 'option_params')

    # initialize database
    # DbSessionFactory.global_init()
    Repository.init(config)
    serve(endpoint, 10)


if __name__ == '__main__':
    main()
