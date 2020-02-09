import os
import sys

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))

import pytest

from data.db_factory import DbSessionFactory
from data.repository import Repository


@pytest.fixture(scope="module")
def init():
    DbSessionFactory.global_init()


def test_historical_data_for_stock_in_period(init):
    historical_data = Repository.historical_data_for_stock_in_period('PAYC', '20190901', '20190910')
    print(historical_data)
