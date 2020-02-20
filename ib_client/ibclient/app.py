import argparse
import logging
import os
from threading import Thread

import time
from datetime import datetime

import logbook
from ddtrace import tracer

from container import Container
from connection_manager.connection_manager import ConnectionManager
from grpc_service.grpc_service import GrpcServer
from ib_client.ib_client import IbClient
from ibapi.wrapper import EWrapper
from init_app import SetupLogger

from configparser import ConfigParser
from Services.LogService import LogService
from monitoring.monitoring_tool import MonitoringTool
from requestmanager.requestmanager import RequestManager


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

    tracer.configure(
        # hostname='host.docker.internal',
        hostname='localhost',
        port=8126,
    )

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
    task = Thread(target=conn_manager.run, args=())
    task.start()
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
