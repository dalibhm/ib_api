import argparse
import os
# import sys
from threading import Thread

from grpc_files.grpc_service import serve
from init_app import init_ib_client

from configparser import ConfigParser
from Services.LogService import LogService
from requestmanager.requestmanager import RequestManager


def main():
    args = parse_args()
    config = init_config(args.mode)
    init_logging(config)

    request_manager = RequestManager()

    ib_client = init_ib_client(config, request_manager)

    app_thread = Thread(target=ib_client.run)
    app_thread.start()



    grpc_thread = Thread(target=serve, args=(ib_client, config, request_manager, 10))
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


def init_config(mode: str):
    config = ConfigParser()
    if mode.lower() in ['dev', 'development', 'development.ini']:
        config.read(os.path.join('..', 'settings', 'development.ini'))
    else:
        raise NotImplementedError
    return config


def init_logging(config):
    # settings = config.get_settings()
    log_level = config.get('logging', 'log_level')
    log_filename = config.get('logging', 'log_filename')

    # Here the LogBook app logger is instanciated
    # to be distinguished from the logbook log of the IBAPI client
    LogService.global_init(log_level, log_filename)


if __name__ == '__main__':
    main()
