import os
from configparser import ConfigParser
from queue import Queue

from ibapi.wrapper import EWrapper
from injector import Injector, singleton

from Services.request_id_generator import RequestIdGenerator
from connection_manager.connection_manager import ConnectionManager
from connection_manager.impl.connection_manager_impl import ConnectionManagerImpl
from ewrapper_impl import EWrapperImpl
from grpc_service.grpc_service import GrpcServer
from ib_client.ib_client import IbClient
from ib_client.impl.ib_client_impl import IbClientImpl
from monitoring.monitoring_tool import MonitoringTool
from requestmanager.cache import Cache
from requestmanager.requestmanager import RequestManager
from requestmanager.status import Status
from responsemanager import FundamentalDataProcessor, GrpcFundamentalDataProcessor, HistoricalDataProcessor, \
    KafkaHistoricalDataProcessor, ContractDetailsProcessor, GrpcContractDetailsProcessor, OptionParamsProcessor, \
    GrpcOptionParamsProcessor, ResponseManager


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