import argparse

from injector import Injector

from configuration.contract_details_config import ContractDetailsModule
from configuration.fundamental_config import FundamentalModule
from configuration.historical_config import HistoricalModule
from configuration.runner_config import RunnerModule
from download_runner.historical_params import HistoricalParams
from scope import Scope


def set_up() -> Injector:
    # parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--type", dest='run_type', required=True,
                        choices={'historical', 'fundamental', 'contract'},
                        action='store', help="request run type")
    parser.add_argument("-e", "--exchanges", dest='exchanges', action='append', help="exchanges to run")
    parser.add_argument("-s", "--stocks", dest='stocks', action='append', help="stocks to run")

    parser.add_argument("--start-date", dest='start_date', action='store', help="start date")
    parser.add_argument("--end-date", dest='end_date', action='store', help="end date")
    parser.add_argument("--stock-number", help="maximal number of stocks to be processed", action='store')
    args = parser.parse_args()

    scope = Scope(stocks=args.stocks, exchanges=args.exchanges)
    if args.run_type == 'historical':
        historical_params = HistoricalParams(start_date=args.start_date, end_date=args.end_date)
        injector = Injector([RunnerModule(scope=scope), HistoricalModule(historical_params=historical_params)])
    if args.run_type == 'fundamental':
        injector = Injector([RunnerModule(scope=scope), FundamentalModule])
    if args.run_type == 'contract':
        injector = Injector([RunnerModule(scope=scope), ContractDetailsModule])
    return injector
