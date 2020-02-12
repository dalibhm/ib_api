# ! [socket_init]
import logging
from configparser import ConfigParser

from ibapi.client import EClient
from ibapi.common import BarData, TickerId
from ibapi.contract import Contract
from ibapi.wrapper import EWrapper
from injector import inject

logger = logging.getLogger()


class IbClientMock(EClient):
    @inject
    def __init__(self, wrapper: EWrapper):
        super().__init__(wrapper)
        # ! [socket_init]
        self.nKeybInt = 0
        # self.started = False
        self.nextValidOrderId = None

    def keyboardInterrupt(self):
        self.nKeybInt += 1
        if self.nKeybInt == 1:
            self.stop()

    def nextOrderId(self):
        oid = self.nextValidOrderId
        self.nextValidOrderId += 1
        return oid

    def connect(self, host, port, clientId):
        print('[ connected to {}:{} as client {} ]'.format(host, port, clientId))

    def reqHistoricalData(self, reqId: TickerId, contract: Contract, endDateTime: str,
                          durationStr: str, barSizeSetting: str, whatToShow: str,
                          useRTH: int, formatDate: int, keepUpToDate: bool, chartOptions: TagValueList):
        print(
            f'[ sent historical data request : {reqId} {contract} {endDateTime} {durationStr} {barSizeSetting} {whatToShow} {useRTH} {formatDate} {keepUpToDate} {chartOptions}]')

        result = BarData()
        result.date = "20191220"
        result.open = 1.
        result.high = 2.
        result.low = 0.
        result.close = 2.
        result.volume = 100
        result.barCount = 2
        result.average = 1.
        self.wrapper.historicalData(reqId, result)
        self.wrapper.historicalDataEnd(reqId=reqId, start="20191220", end="20191220")
