import os
from configparser import ConfigParser
from pytest import fixture

from injector import Injector, singleton

from input_manager.impl.static_list import PostgresConnect
from input_manager.input_manager import InputManager


class TestContainer:
    def __init__(self):
        environment = os.getenv('environment') or 'development'
        self.config = ConfigParser()
        self.config.read(os.path.join('settings', environment + '.ini'))
        self.injector = Injector(self.configure, auto_bind=False)

    def configure(self, binder):
        binder.bind(ConfigParser, to=self.config, scope=singleton)
        binder.bind(str, to="nyse", scope=singleton)
        binder.bind(InputManager, to=PostgresConnect, scope=singleton)


@fixture
def _injector():
    test_container = TestContainer()
    return test_container.injector


def test_postgres_connect(_injector):
    postgres_connect: PostgresConnect = _injector.get(InputManager)
    stocks = postgres_connect.stock_list
    assert len(stocks) > 0
