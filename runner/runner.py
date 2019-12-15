import logging
import time
from configparser import ConfigParser
import argparse
import json
import os

from download_runner.kafka_download_runner_factory import KafkaDownloadRunnerFactory

from services.fundamental_service import FundamentalService
from services.historical_data_service import HistoricalDataService
from services.ib_client import IbClient
from services.listing_service import ListingService


def main():
    """
    reads the configuration file
    connects to services
    run the DownloadRunner with the configuration requested
    :return: 
    """

    # load configuration
    environment = os.getenv('environment') or 'development'
    config = ConfigParser()
    config.read(os.path.join('settings', environment + '.ini'))
    filename = config.get('data config', 'file')

    # with open(os.path.join('.', 'settings', filename), 'r') as f:
    #     download_config = json.load(f)

    # configure services
    services = {
        'ib': IbClient(config.get('services', 'ib')),
        # stock-listing service retrieves the stock properties / the index constituents
        'listing': ListingService(config.get('services', 'stock_listing')),
        'historical_data': HistoricalDataService(config.get('services', 'historical_data')),
        # fundamental service checks the last available financial report
        # in order to decide weather to launch a request or not, if the report has not changed
        'fundamental': FundamentalService(config.get('services', 'fundamental_data'))
    }

    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-hist", "--historical", help="run historical data requests", action='store_true')
    parser.add_argument("-f", "--fundamental", help="run fundamental data requests", action='store_true')
    parser.add_argument("--start-date", help="start date", action='store')
    parser.add_argument("--end-date", help="end date", action='store')
    parser.add_argument("--stock-number", help="maximal number of stocks to be processed", action='store')
    args = parser.parse_args()

    # configure logging
    if not os.path.exists("log"):
        os.makedirs("log")

    FORMAT = '%(asctime)-15s %(levelname)s %(name)-s %(message)s'
    logging.basicConfig(filename=time.strftime(os.path.join("log", "runner_%Y%m%d_%H_%M_%S.log")),
                        filemode="w",
                        level=logging.DEBUG,
                        format=FORMAT)

    # run program
    # runner_manager = DownloadRunner(download_config, services)
    runner_manager = KafkaDownloadRunnerFactory.create(services, args, config)
    runner_manager.run()


if __name__ == '__main__':
    print('Runner starting...')
    main()
