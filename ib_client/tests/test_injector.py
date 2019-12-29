import pytest
from injector import Injector, inject, singleton

from Services.request_id_generator import RequestIdGenerator
from connection_manager.connection_manager import ConnectionManager
from ibapi.wrapper import EWrapper
from api.ib_client import IbClient
from requestmanager.requestmanager import RequestsLimit, RequestManager


class IdGenTest(RequestIdGenerator):
    pass


class ConnTest(ConnectionManager):
    pass


class RequestLimitTest(RequestsLimit):
    pass


class ClientTest(IbClient):
    @inject
    def __init__(self, wrapper: EWrapper):
        super().__init__(wrapper)


class WrapperTest(EWrapper):
    pass


def configure(binder):
    binder.bind(RequestIdGenerator, to=IdGenTest, scope=singleton)
    binder.bind(ConnectionManager, to=ConnTest, scope=singleton)
    binder.bind(RequestsLimit, to=RequestsLimit, scope=singleton)
    binder.bind(EWrapper, to=WrapperTest, scope=singleton)
    binder.bind(IbClient, to=ClientTest, scope=singleton)
    binder.bind(RequestManager, to=RequestManager, scope=singleton)


def test_connectionmanager():
    injector = Injector(configure)
    connection_manager = injector.get(ConnectionManager)
    assert type(connection_manager) == ConnTest


# @pytest.mark.skip
def test_requestmanager():
    injector = Injector(configure)
    request_manager = injector.get(RequestManager)

    assert type(request_manager.request_id_gen) == IdGenTest
    assert type(request_manager._connection_manager) == ConnTest
    assert type(request_manager.requests_limit) == RequestsLimit
    assert type(request_manager.ib_client) == ClientTest
