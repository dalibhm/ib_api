# ! [socket_init]
import collections
import datetime
import logging
from configparser import ConfigParser

from ibapi.client import EClient


from ewrapper_impl import EWrapperImpl
from ib_response_manager.grpc_reponse_manager import GrpcResponseManager
from ib_response_manager.response_processor_factory import ResponseProcessorFactory

logger = logging.getLogger()


class IbClient(EClient):

    def __init__(self, config: ConfigParser, request_manager):
        self.connection_manager = None
        wrapper = EWrapperImpl(config=config, request_manager=request_manager)

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

    def register_connection_manager(self, connection_manager):
        self.connection_manager = connection_manager
        self.wrapper.connection_manager = connection_manager
