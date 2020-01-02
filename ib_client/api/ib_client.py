from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class IbClient(EClient):
    def __init__(self, wrapper: EWrapper):
        super().__init__(wrapper)
        # ! [socket_init]
        self.nKeybInt = 0
        # self.started = False
        self.nextValidOrderId = None

    def stop(self):
        pass

    def nextOrderId(self):
        oid = self.nextValidOrderId
        self.nextValidOrderId += 1
        return oid
