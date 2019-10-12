import time
from unittest import TestCase

from ibapi import Contract

from tests import init_application


class TestReqFundamentalData(TestCase):
    def test(self):
        contract = Contract()
        contract.symbol = "IBKR"
        contract.secType = "STK"
        contract.currency = "USD"
        contract.exchange = "ISLAND"
        app = init_application()

        time.sleep(5)

        app.reqFundamentalData(1000, contract, 'ReportsFinSummary', [])

        time.sleep(100)
