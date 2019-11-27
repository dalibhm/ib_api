from configparser import ConfigParser
import json
import os

# from data_api import DataApiClient
from download_runner import DownloadRunner
from kafka_download_runner import KafkaDownloadRunner
from services.fundamental_service import FundamentalService
from services.ib_client import IbClient
from services.listing_service import ListingService


def main():
    """
    reads the configuration file
    connects to services
    run the DownloadRunner with the configuration requested
    :return: 
    """
    config = ConfigParser()
    config.read(os.path.join('..', 'settings', 'development.ini'))
    filename = config.get('data config','file')

    with open(os.path.join('.', 'settings', filename), 'r') as f:
        download_config = json.load(f)

    services = {
        'ib': IbClient(config.get('services', 'ib')),
        # stock-listing service retrieves the stock properties / the index constituents
        'listing': ListingService(config.get('services', 'stock_listing')),
        # fundamental service checks the last available financial report
        # in order to decide weather to launch a request or not, if the report has not changed
        'fundamental': FundamentalService(config.get('services', 'fundamental_data'))
    }
    # runner_manager = DownloadRunner(download_config, services)
    runner_manager = KafkaDownloadRunner(services, config=config)
    runner_manager.go()


if __name__ == '__main__':
    print('Runner starting')
    main()
