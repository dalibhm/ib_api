import argparse
import logging
import os
# import sys
import time
from datetime import datetime
from queue import Queue

import logbook

from Services.request_id_generator import RequestIdGenerator
from api.impl.ib_client_impl import IbClientImpl
from connection_manager.connection_manager import ConnectionManager
from connection_manager.impl.connection_manager_impl import ConnectionManagerImpl
from ewrapper_impl import EWrapperImpl
from grpc_service.grpc_service import GrpcServer
from api.ib_client import IbClient
from ibapi.wrapper import EWrapper
from init_app import SetupLogger

from configparser import ConfigParser
from Services.LogService import LogService
from monitoring.monitoring_tool import MonitoringTool
from requestmanager.cache import Cache
# from requestmanager.request_scheduler import RequestScheduler
from requestmanager.requestmanager import RequestManager

from injector import Injector, singleton

from requestmanager.status import Status
from responsemanager import GrpcContractDetailsProcessor
from responsemanager import ContractDetailsProcessor
from responsemanager.fundamental_data_processor_impl.grpc_fundamental_processor import GrpcFundamentalDataProcessor
from responsemanager import FundamentalDataProcessor
from responsemanager import HistoricalDataProcessor
from responsemanager import KafkaHistoricalDataProcessor
from responsemanager import GrpcOptionParamsProcessor
from responsemanager import OptionParamsProcessor
from responsemanager import ResponseManager


class Container:
    def __init__(self):
        environment = os.getenv('environment') or 'development'
        self.config = ConfigParser()
        self.config.read(os.path.join('../settings', environment + '.ini'))
        self.injector = Injector(self.configure, auto_bind=False)

    def configure(self, binder):
        binder.bind(ConfigParser, to=self.config, scope=singleton)
        binder.bind(RequestIdGenerator, to=RequestIdGenerator, scope=singleton)
        binder.bind(ConnectionManager, to=ConnectionManagerImpl, scope=singleton)
        # binder.bind(RequestsLimit, to=RequestsLimit, scope=singleton)
        binder.bind(EWrapper, to=EWrapperImpl, scope=singleton)
        binder.bind(IbClient, to=IbClientImpl, scope=singleton)
        binder.bind(RequestManager, to=RequestManager, scope=singleton)

        binder.bind(Cache, to=Cache, scope=singleton)
        binder.bind(Status, to=Status, scope=singleton)
        binder.bind(Queue, to=Queue, scope=singleton)

        # binder.bind(RequestScheduler, to=RequestScheduler, scope=singleton)
        binder.bind(MonitoringTool, to=MonitoringTool, scope=singleton)

        # data processors / response manager
        # binder.bind(FundamentalDataProcessor, to=ConsoleFundamentalDataProcessor, scope=singleton)
        binder.bind(FundamentalDataProcessor, to=GrpcFundamentalDataProcessor, scope=singleton)
        # binder.bind(HistoricalDataProcessor, to=ConsoleHistoricalDataProcessor, scope=singleton)
        binder.bind(HistoricalDataProcessor, to=KafkaHistoricalDataProcessor, scope=singleton)
        # binder.bind(HistoricalDataProcessor, to=KafkaHistoricalDataProcessor, scope=singleton)
        # binder.bind(ContractDetailsProcessor, to=ContractDetailsProcessorImpl, scope=singleton)
        binder.bind(ContractDetailsProcessor, to=GrpcContractDetailsProcessor, scope=singleton)
        binder.bind(OptionParamsProcessor, to=GrpcOptionParamsProcessor, scope=singleton)
        binder.bind(ResponseManager, to=ResponseManager, scope=singleton)

        binder.bind(GrpcServer, to=GrpcServer, scope=singleton)

    # def get(self, class_):
    #     instance = self.injector(class_)


def main():
    args = parse_args()

    # api logging
    SetupLogger()
    logger = logging.getLogger()
    logger.debug("now is %s", datetime.now())
    logger.setLevel(logging.INFO)

    #

    container = Container()
    injector = container.injector

    config = injector.get(ConfigParser)
    # app logging
    init_logging(config)
    logger: logbook.Logger = LogService.get_startup_log()
    # construct client
    ib_client = injector.get(IbClient)
    # ib_client.globalCancelOnly = confiig.getboolean('ib client', 'global-cancel')

    # connection manager
    conn_manager = injector.get(ConnectionManager)
    logger.debug('Created ConnectionManager Instance')
    request_manager = injector.get(RequestManager)
    logger.debug('Created RequestManager Instance')

    monitoring_tool = injector.get(MonitoringTool)

    wrapper = injector.get(EWrapper)
    wrapper.connection_manager = conn_manager
    wrapper.request_manager = request_manager
    logger.debug('Added ConnectionManager and RequestManager Instances to EWrapper')

    # starts connection manager
    # connect automatically
    logger.debug('Starting ConnectionManager')
    conn_manager.start()
    logger.debug('Started ConnectionManager')
    time.sleep(2)

    grpc_server = injector.get(GrpcServer)
    logger.debug('Started GRPC Service')


def parse_args():
    cmdLineParser = argparse.ArgumentParser("api tests")
    cmdLineParser.add_argument("-m", "--mode", action="store", type=str,
                               dest="mode", default="development",
                               help="Config mode : development, integration or production")
    # cmdLineParser.add_option("-c", action="store_True", dest="use_cache", default = False, help = "use the cache")
    # cmdLineParser.add_option("-f", action="store", type="string", dest="file", default="", help="the input file")
    cmdLineParser.add_argument("-p", "--port", action="store", type=int,
                               dest="port", default=7496, help="The TCP port to use")
    cmdLineParser.add_argument("-i", "--ib-host", action="store", type=str,
                               dest="host", default="127.0.0.1", help="ib api host ip address")
    cmdLineParser.add_argument("-C", "--global-cancel", action="store_true",
                               dest="global_cancel", default=False,
                               help="whether to trigger a globalCancel req")
    return cmdLineParser.parse_args()


def init_logging(config):
    # settings = config.get_settings()
    log_level = config.get('logging', 'log_level')
    log_filename = config.get('logging', 'log_filename')

    # Here the LogBook app logger is instanciated
    # to be distinguished from the logbook log of the IBAPI client
    LogService.global_init(log_level, os.path.join('..', 'log', log_filename))


if __name__ == '__main__':
    main()