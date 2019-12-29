import datetime
import logging
from configparser import ConfigParser

from ibapi.common import BarData, ListOfHistoricalTick, ListOfHistoricalTickBidAsk, TickerId, ListOfHistoricalTickLast, \
    OrderId
from ibapi.contract import ContractDetails, Contract
from ibapi.order import Order
from ibapi.order_state import OrderState
from ibapi.wrapper import EWrapper
from injector import inject

from ib_response_manager.grpc.grpc_reponse_manager import GrpcResponseManager
from ib_response_manager.response_processor_factory import ResponseProcessorFactory
from requestmanager.requestmanager import RequestManager

logger = logging.getLogger(__name__)


class EWrapperImpl(EWrapper):
    @inject
    def __init__(self, config: ConfigParser):
        super().__init__()
        self.asynchronous = False

        # if injected, the two classes below induce circular references as they depend on ib_client
        # which holds a reference to EWrapper
        self.connection_manager = None
        self.request_manager: RequestManager = None


    # ! [connectack]
    def connectAck(self):
        if self.asynchronous:
            self.startApi()

    # ! [connectack]

    # ! [nextvalidid]
    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)

        logger.debug("setting nextValidOrderId: %d", orderId)
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)
        # ! [nextvalidid]

        # we can start now
        # self.start()

    def connectionClosed(self):
        """This function is called when TWS closes the sockets
        connection with the ActiveX control, or when TWS is shut down."""

        super().connectionClosed()
        # as the connection is closed, reconnect
        self.connection_manager.connection_closed = True

    # ! [currenttime]
    def currentTime(self, time: int):
        super().currentTime(time)
        print("CurrentTime:", datetime.datetime.fromtimestamp(time).strftime("%Y%m%d %H:%M:%S"))

    # ! [currenttime]

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        super().contractDetails(reqId, contractDetails)
        self.response_processor.process_contract_details(contractDetails)

    # ! [contractdetails]

    # ! [contractdetailsend]
    def contractDetailsEnd(self, reqId: int):
        super().contractDetailsEnd(reqId)
        print("ContractDetailsEnd. ReqId:", reqId)

    # ! [contractdetailsend]

    # ! [headTimestamp]
    def headTimestamp(self, reqId: int, headTimestamp: str):
        print("HeadTimestamp. ReqId:", reqId, "HeadTimeStamp:", headTimestamp)

    # ! [headTimestamp]

    # ! [historicaldata]
    def historicalData(self, reqId: int, bar: BarData):
        # print("HistoricalData. ReqId:", reqId, "BarData.", bar)
        # self.response_processor.process_historical_data(reqId, bar)
        self.request_manager.process_historical_data(reqId, bar)

    # ! [historicaldata]

    # ! [historicaldataend]
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)

        self.response_processor.process_historical_data_end(reqId, start, end)
        self.request_manager.process_historical_data_end(reqId, start, end)

    # ! [historicaldataend]

    # ! [historicalDataUpdate]
    def historicalDataUpdate(self, reqId: int, bar: BarData):
        print("HistoricalDataUpdate. ReqId:", reqId, "BarData.", bar)

    # ! [historicalDataUpdate]

    # ! [historicalticks]
    def historicalTicks(self, reqId: int, ticks: ListOfHistoricalTick, done: bool):
        for tick in ticks:
            print("HistoricalTick. ReqId:", reqId, tick)

    # ! [historicalticks]

    # ! [historicalticksbidask]
    def historicalTicksBidAsk(self, reqId: int, ticks: ListOfHistoricalTickBidAsk,
                              done: bool):
        for tick in ticks:
            print("HistoricalTickBidAsk. ReqId:", reqId, tick)

    # ! [historicalticksbidask]

    # ! [historicaltickslast]
    def historicalTicksLast(self, reqId: int, ticks: ListOfHistoricalTickLast,
                            done: bool):
        for tick in ticks:
            print("HistoricalTickLast. ReqId:", reqId, tick)

    # ! [historicaltickslast]

    # ! [fundamentaldata]
    def fundamentalData(self, reqId: TickerId, data: str):
        super().fundamentalData(reqId, data)

        self.request_manager.on_request_end(reqId, 'fundamental')
        logger.info('{} {} {}'.format(reqId, request.reportType, request.contract.symbol))
        self.fundamental_response_manager.process_financial_data(request, data)

    # ! [fundamentaldata]

    # ! [error]
    def error(self, reqId: TickerId, errorCode: int, errorString: str):
        super().error(reqId, errorCode, errorString)

        # historical data error
        # this needs to be treated in a generic way as the error codes may not be
        # specific to request type

        if errorCode in [err for err in range(501, 505)]:
            print(reqId, errorCode, errorString[:50])
        else:
            self.request_manager.process_error(reqId, errorCode, errorString)
        # self.response_processor.process_historical_error(reqId, errorCode, errorString)


   # ! [error] self.reqId2nErr[reqId] += 1

    def winError(self, text: str, lastError: int):
        super().winError(text, lastError)

    # ! [openorder]
    def openOrder(self, orderId: OrderId, contract: Contract, order: Order,
                  orderState: OrderState):
        super().openOrder(orderId, contract, order, orderState)
        print("OpenOrder. ID:", orderId, "Symbol:", contract.symbol, "SecType:", contract.secType,
              "Exchange:", contract.exchange, "Action:", order.action, "OrderType:", order.orderType,
              "TotalQuantity:", order.totalQuantity, "Status:", orderState.status)

        if order.whatIf and orderState is not None:
            print("WhatIf. OrderId: ", orderId, "initMarginBefore:", orderState.initMarginBefore, "maintMarginBefore:",
                  orderState.maintMarginBefore,
                  "equityWithLoanBefore:", orderState.equityWithLoanBefore, "initMarginChange:",
                  orderState.initMarginChange, "maintMarginChange:", orderState.maintMarginChange,
                  "equityWithLoanChange:", orderState.equityWithLoanChange, "initMarginAfter:",
                  orderState.initMarginAfter, "maintMarginAfter:", orderState.maintMarginAfter,
                  "equityWithLoanAfter:", orderState.equityWithLoanAfter)

        order.contract = contract
        self.permId2ord[order.permId] = order

    # ! [openorder]

    # ! [openorderend]
    def openOrderEnd(self):
        super().openOrderEnd()
        print("OpenOrderEnd")

        logger.debug("Received %d openOrders", len(self.permId2ord))

    # ! [openorderend]

    # ! [orderstatus]
    def orderStatus(self, orderId: OrderId, status: str, filled: float,
                    remaining: float, avgFillPrice: float, permId: int,
                    parentId: int, lastFillPrice: float, clientId: int,
                    whyHeld: str, mktCapPrice: float):
        super().orderStatus(orderId, status, filled, remaining,
                            avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice)
        print("OrderStatus. Id:", orderId, "Status:", status, "Filled:", filled,
              "Remaining:", remaining, "AvgFillPrice:", avgFillPrice,
              "PermId:", permId, "ParentId:", parentId, "LastFillPrice:",
              lastFillPrice, "ClientId:", clientId, "WhyHeld:",
              whyHeld, "MktCapPrice:", mktCapPrice)

    # ! [orderstatus]
