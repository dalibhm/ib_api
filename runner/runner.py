from configparser import ConfigParser
import json
import os

# from data_api import DataApiClient
from download_runner import DownloadRunner
from services.ib_client import IbClient
from services.listing_service import ListingService


def main():
    config = ConfigParser()
    config.read(os.path.join('..', 'settings', 'development.ini')
    filename = config.get('data config','file')
    with open(os.path.join('.', 'settings', filename), 'r') as f:
        download_config = json.load(f)

    ib_server_url = config.get('services','ib')

    ib_client = IbClient(ib_server_url)
    listing_service = ListingService(config.get('services', 'stock_listing'))
    runner_manager = DownloadRunner(download_config, ib_client, listing_service)
    runner_manager.go()


if __name__ == '__main__':
    print('Runner starting')
    main()
