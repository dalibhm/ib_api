import pytest

import tests
from configparser import ConfigParser


from data.repository import Repository
from data.option_params import OptionParams


@pytest.fixture(scope="module")
def repository():
    config = ConfigParser()
    config.add_section('postgres')
    config.set('postgres', 'user', 'ib_test'),
    config.set('postgres', 'password', 'ib_test')
    config.set('postgres', 'host', 'localhost')
    config.set('postgres', 'port', '5432')
    config.set('postgres', 'db', 'ib_test')
    config.set('postgres', 'echo', 'True')
    Repository.init(config)


def test_add_option_params(repository):
    record = OptionParams(exchange='exchange',
                          underlyingConId=123,
                          tradingClass='td',
                          multiplier=100,
                          expirations={'213', '234'},
                          strikes={1, 2, 4})
    Repository.add_option_params(record)


@pytest.mark.skip
def test_get_option_params(repository):
    op = Repository.get_option_params(123)
    assert 'exchange' == op.exchange
