import logging
from configparser import ConfigParser
from datetime import datetime
from threading import Thread

from ibclient.ib_client.impl.ib_client_impl import IbClientImpl
from ibclient.connection_manager.impl.connection_manager_impl import ConnectionManagerImpl
from ibclient.enums.request_type import RequestType
from ibclient.ewrapper_impl import EWrapperImpl
from ibclient.init_app import SetupLogger
from ibclient.responsemanager import ContractDetailsProcessorImpl
from ibclient.responsemanager import ContractDetailsProcessor
from ibclient.responsemanager.fundamental_data_processor_impl.grpc_fundamental_processor import GrpcFundamentalDataProcessor
from ibclient.responsemanager import FundamentalDataProcessor
from ibclient.responsemanager import HistoricalDataProcessor
from ibclient.responsemanager import ConsoleHistoricalDataProcessor
from ibclient.responsemanager import GrpcOptionParamsProcessor
from ibclient.responsemanager import OptionParamsProcessor
from ibclient.responsemanager import ResponseManager
from ibclient.tests import *


def configure(binder):
    environment = 'development'
    config = ConfigParser()
    config.read(os.path.join('', 'settings', environment + '.ini'))
    binder.bind(ConfigParser, to=config, scope=singleton)

    binder.bind(RequestIdGenerator, to=RequestIdGenerator, scope=singleton)
    binder.bind(ConnectionManager, to=ConnectionManagerImpl, scope=singleton)
    binder.bind(EWrapper, to=EWrapperImpl, scope=singleton)
    binder.bind(IbClient, to=IbClientImpl, scope=singleton)
    binder.bind(RequestManager, to=RequestManager, scope=singleton)

    # data processors / response manager
    binder.bind(FundamentalDataProcessor, to=GrpcFundamentalDataProcessor, scope=singleton)
    binder.bind(HistoricalDataProcessor, to=ConsoleHistoricalDataProcessor, scope=singleton)
    binder.bind(ContractDetailsProcessor, to=ContractDetailsProcessorImpl, scope=singleton)
    binder.bind(OptionParamsProcessor, to=GrpcOptionParamsProcessor, scope=singleton)
    binder.bind(ResponseManager, to=ResponseManager, scope=singleton)

def read_stocks():
    stocks = []
    with open('ibclient/tests/stocks_amex.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stocks.append(row)
    return stocks

def sample_historical_request():
    contracts = read_stocks()
    request = historical_request(contracts[0])
    return request


def main():

    injector = Injector(configure)

    # api logging
    SetupLogger()
    logger = logging.getLogger()
    logger.debug("now is %s", datetime.now())
    logger.setLevel(logging.DEBUG)

    ib_client = injector.get(IbClient)

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

    # while not conn_manager.is_connected():
    #     continue

    contracts = read_stocks()
    for contract in contracts[:50]:
        request = contract_details_request(contract)

        request_manager.add_request(request, RequestType.ContractDetails)
    # request = contract_details_request(contracts[0])
    # request.contract.secType = "OPT";
    # request.contract.exchange = "SMART";
    # request_manager.add_request(request, RequestType.ContractDetails)

    app_thread.join()


if __name__ == '__main__':
    main()
