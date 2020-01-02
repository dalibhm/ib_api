import logging
from configparser import ConfigParser
from datetime import datetime
from threading import Thread

from api.impl.ib_client_impl import IbClientImpl
from app import init_logging
from connection_manager.impl.connection_manager_impl import ConnectionManagerImpl
from enums.request_type import RequestType
from ewrapper_impl import EWrapperImpl
from init_app import SetupLogger
from responsemanager.contact_details_processor_impl.contract_details_processor import ContractDetailsProcessorImpl
from responsemanager.contact_details_processor_impl.grpc_contract_details_processor import GrpcContractDetailsProcessor
from responsemanager.contract_details_processor import ContractDetailsProcessor
from responsemanager.fundamental_data_processor_impl.grpc_fundamental_processor import GrpcFundamentalDataProcessor
from responsemanager.fundamental_processor import FundamentalDataProcessor
from responsemanager.historical_processor import HistoricalDataProcessor
from responsemanager.historical_processor_impl.console_historical_processor import ConsoleHistoricalDataProcessor
from responsemanager.historical_processor_impl.kafka_historical_processor import KafkaHistoricalDataProcessor
from responsemanager.option_param_processor_impl.grpc_option_params_processor import GrpcOptionParamsProcessor
from responsemanager.option_params_processor import OptionParamsProcessor
from responsemanager.response_manager import ResponseManager
from tests import *


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
    binder.bind(ContractDetailsProcessor, to=GrpcContractDetailsProcessor, scope=singleton)
    binder.bind(OptionParamsProcessor, to=GrpcOptionParamsProcessor, scope=singleton)
    binder.bind(ResponseManager, to=ResponseManager, scope=singleton)

def read_stocks():
    stocks = []
    with open('tests/stocks_amex.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stocks.append(row)
    return stocks

def sample_historical_request():
    contracts = read_stocks()
    request = historical_request(contracts[0])
    return request


def main():
    contracts = read_stocks()
    contract = contracts[1]
    request = contract_details_request(contract)

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

    request_manager.add_request(request, RequestType.ContractDetails)
    # request = contract_details_request(contracts[0])
    # request.contract.secType = "OPT";
    # request.contract.exchange = "SMART";
    # request_manager.add_request(request, RequestType.ContractDetails)

    app_thread.join()


if __name__ == '__main__':
    main()
