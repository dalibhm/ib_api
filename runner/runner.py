import logging
import time
from configparser import ConfigParser
import argparse
import json
import os

from injector import Injector


from configuration.contract_details_config import ContractDetailsModule
from configuration.historical_config import HistoricalModule
from configuration.runner_config import RunnerModule
from configuration.set_up import set_up
from download_manager.download_manager import DownloadManager
from download_runner.impl.historical_runner import HistoricalRunner
from download_runner.kafka_download_runner_factory import KafkaDownloadRunnerFactory


from services.fundamental_service import FundamentalService
from services.historical_data_service import HistoricalDataService
from services.ib_client import IbClient


def main():
    """
    reads the configuration file
    connects to services
    run the DownloadRunner with the configuration requested
    :return: 
    """
    # configure logging
    if not os.path.exists("log"):
        os.makedirs("log")
        
    FORMAT = '%(asctime)-15s %(levelname)s %(name)-s:%(lineno)d %(message)s'
    logging.basicConfig(filename=time.strftime(os.path.join("log", "runner_%Y%m%d_%H_%M_%S.log")),
                        filemode="w",
                        level=logging.DEBUG,
                        format=FORMAT)


        # 'fundamental': FundamentalService(config.get('services', 'fundamental_data'))




    # scope = Scope(stocks=args.stocks, exchanges=args.exchanges)

    injector = set_up()

    # run program

    download_manager = injector.get(DownloadManager)
    # runner_manager = KafkaDownloadRunnerFactory.create(services, args, config)
    download_manager.run()


if __name__ == '__main__':
    print('Runner starting...')
    main()
