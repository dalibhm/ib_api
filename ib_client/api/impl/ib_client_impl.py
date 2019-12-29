# ! [socket_init]
import logging
from configparser import ConfigParser

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from injector import inject

logger = logging.getLogger()


class IbClientImpl(EClient):
    @inject
    def __init__(self, wrapper: EWrapper):
        super().__init__(wrapper)
        # ! [socket_init]
        self.nKeybInt = 0
        # self.started = False
        self.nextValidOrderId = None

    # def start(self):
    #     if self.started:
    #         return
    #
    #     self.started = True
    #
    #     if self.globalCancelOnly:
    #         print("Executing GlobalCancel only")
    #         self.reqGlobalCancel()

    def keyboardInterrupt(self):
        self.nKeybInt += 1
        if self.nKeybInt == 1:
            self.stop()

    def stop(self):
        print("Executing cancels")
        # put something here to cancel issued orders
        print("Executing cancels ... finished")

    def nextOrderId(self):
        oid = self.nextValidOrderId
        self.nextValidOrderId += 1
        return oid
