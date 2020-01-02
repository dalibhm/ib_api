from configparser import ConfigParser

from enums.request_type import RequestType
from responsemanager.contact_details_processor_impl.contract_details_processor import ContractDetailsProcessorImpl
from responsemanager.contract_details_processor import ContractDetailsProcessor
from responsemanager.fundamental_data_processor_impl.grpc_fundamental_processor import GrpcFundamentalDataProcessor
from responsemanager.fundamental_processor import FundamentalDataProcessor
from responsemanager.historical_processor import HistoricalDataProcessor
from responsemanager.historical_processor_impl.kafka_historical_processor import KafkaHistoricalDataProcessor
from responsemanager.response_manager import ResponseManager
from tests import *


def configure(binder):
    config = ConfigParser()
    environment = 'development'
    config = ConfigParser()
    config.read(os.path.join('..', 'settings', environment + '.ini'))
    binder.bind(ConfigParser, to=config, scope=singleton)

    binder.bind(RequestIdGenerator, to=IdGenTest, scope=singleton)
    binder.bind(ConnectionManager, to=ConnTest, scope=singleton)
    binder.bind(EWrapper, to=WrapperTest, scope=singleton)
    binder.bind(IbClient, to=ClientTest, scope=singleton)
    binder.bind(RequestManager, to=RequestManager, scope=singleton)

    # data processors / response manager
    binder.bind(FundamentalDataProcessor, to=GrpcFundamentalDataProcessor, scope=singleton)
    binder.bind(HistoricalDataProcessor, to=KafkaHistoricalDataProcessor, scope=singleton)
    binder.bind(ContractDetailsProcessor, to=ContractDetailsProcessorImpl, scope=singleton)
    binder.bind(ResponseManager, to=ResponseManager, scope=singleton)


def test_connectionmanager():
    injector = Injector(configure)
    connection_manager = injector.get(ConnectionManager)
    assert type(connection_manager) == ConnTest


# @pytest.mark.skip
def test_request_manager():
    injector = Injector(configure)
    request_manager = injector.get(RequestManager)

    assert type(request_manager.request_id_gen) == IdGenTest
    assert type(request_manager._connection_manager) == ConnTest
    assert type(request_manager._ib_client) == ClientTest


