from configparser import ConfigParser
import argparse
import json
import os

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
    config = ConfigParser()
    config.read(os.path.join('..', 'settings', 'development.ini'))
    filename = config.get('data config', 'file')

    with open(os.path.join('.', 'settings', filename), 'r') as f:
        download_config = json.load(f)

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

    contract = {"conId": 10089, "symbol": "NAV", "currency": "USD", "exchange": "SMART"}
    request = {"endDateTime": "20191127 00:00:00",
               "durationString": "20 Y",
               "barSizeSetting": "1 day",
               "whatToShow": "TRADES",
               "useRTH": 1,
               "formatDate": 1,
               "keepUpToDate": False}

    services['ib'].request_historical_data(contract, request)


if __name__ == '__main__':
    print('Runner starting...')
    main()
