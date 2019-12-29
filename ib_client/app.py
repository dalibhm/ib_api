import argparse
import logging
import os
# import sys
from datetime import datetime
from threading import Thread

from Services.request_id_generator import RequestIdGenerator
from api.impl.ib_client_impl import IbClientImpl
from connection_manager.connection_manager import ConnectionManager
from connection_manager.impl.connection_manager_impl import ConnectionManagerImpl
from ewrapper_impl import EWrapperImpl
from grpc_service.grpc_service import serve
from api.ib_client import IbClient
from ibapi.wrapper import EWrapper
from init_app import SetupLogger

from configparser import ConfigParser
from Services.LogService import LogService
from requestmanager.requestmanager import RequestManager, RequestsLimit

from injector import Injector, inject, singleton


class Container:
    def __init__(self):
        environment = os.getenv('environment') or 'development'
        self.config = ConfigParser()
        self.config.read(os.path.join('settings', environment + '.ini'))
        self.injector = Injector(self.configure, auto_bind=False)

    def configure(self, binder):
        binder.bind(ConfigParser, to=self.config, scope=singleton)
        binder.bind(RequestIdGenerator, to=RequestIdGenerator, scope=singleton)
        binder.bind(ConnectionManager, to=ConnectionManagerImpl, scope=singleton)
        binder.bind(RequestsLimit, to=RequestsLimit, scope=singleton)
        binder.bind(EWrapper, to=EWrapperImpl, scope=singleton)
        binder.bind(IbClient, to=IbClientImpl, scope=singleton)
        binder.bind(RequestManager, to=RequestManager, scope=singleton)

    # def get(self, class_):
    #     instance = self.injector(class_)



def main():
    args = parse_args()


    # api logging
    SetupLogger()
    logger = logging.getLogger()
    logger.debug("now is %s", datetime.now())
    logger.setLevel(logging.DEBUG)

    #

    container = Container()
    injector = container.injector

    config = injector.get(ConfigParser)
    # app logging
    init_logging(config)
    # construct client
    ib_client = injector.get(IbClient)
    # ib_client.globalCancelOnly = confiig.getboolean('ib client', 'global-cancel')

    # connection manager
    conn_manager = injector.get(ConnectionManager)
    request_manager = injector.get(RequestManager)

    wrapper = injector.get(EWrapper)
    wrapper.connection_manager = conn_manager
    wrapper.request_manager = request_manager


    # run service
    app_thread = Thread(target=ib_client.run)
    app_thread.start()

    # starts connection manager
    # connect automatically
    conn_manager.start()

    grpc_thread = Thread(target=serve, args=(ib_client, config, request_manager, conn_manager))
    grpc_thread.start()


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
    LogService.global_init(log_level, log_filename)


if __name__ == '__main__':
    main()
