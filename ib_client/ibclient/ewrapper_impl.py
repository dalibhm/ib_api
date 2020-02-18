import datetime
import logging
from configparser import ConfigParser
from typing import List

from ddtrace import tracer
from ibapi.common import BarData, ListOfHistoricalTick, ListOfHistoricalTickBidAsk, TickerId, ListOfHistoricalTickLast, \
    OrderId, SetOfString, SetOfFloat
from ibapi.contract import ContractDetails, Contract
from ibapi.order import Order
from ibapi.order_state import OrderState
from ibapi.wrapper import EWrapper
from injector import inject

from requestmanager.requestmanager import RequestManager
from subject import Subject

logger = logging.getLogger(__name__)


class EWrapperImpl(EWrapper, Subject):
    @inject
    def __init__(self, config: ConfigParser):
        super().__init__()
        Subject.__init__(self)
        self.asynchronous = False

        # if injected, the two classes below induce circular references as they depend on ib_client
        # which holds a reference to EWrapper
        self.connection_manager = None
        self.request_manager: RequestManager = None
        # self.requests: List[Request] = []

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

    @tracer.wrap(name='connection closed', service='historical req')
    def connectionClosed(self):
        """This function is called when TWS closes the sockets
        connection with the ActiveX control, or when TWS is shut down."""

        super().connectionClosed()
        # [request.connectionClosed() for request in self.observers]
        # as the connection is closed, reconnect

        self.notify()


    # ! [currenttime]
    def currentTime(self, time: int):
        super().currentTime(time)
        print("CurrentTime:", datetime.datetime.fromtimestamp(time).strftime("%Y%m%d %H:%M:%S"))

    # ! [currenttime]

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        super().contractDetails(reqId, contractDetails)
        self.request_manager.process_data(reqId, contractDetails)

    # ! [contractdetails]

    # ! [contractdetailsend]
    def contractDetailsEnd(self, reqId: int):
        super().contractDetailsEnd(reqId)
        self.request_manager.process_data_end(reqId)
        # [request.process_data_end() for request in self.requests]

    # ! [contractdetailsend]

    # ! [headTimestamp]
    def headTimestamp(self, reqId: int, headTimestamp: str):
        print("HeadTimestamp. ReqId:", reqId, "HeadTimeStamp:", headTimestamp)
        self.request_manager.process_data(reqId, headTimestamp)

    # ! [headTimestamp]

    # ! [historicaldata]
    def historicalData(self, reqId: int, bar: BarData):
        # print("HistoricalData. ReqId:", reqId, "BarData.", bar)
        # self.response_processor.process_historical_data(reqId, bar)
        self.request_manager.process_data(reqId, bar)

    # ! [historicaldata]

    # ! [historicaldataend]
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)

        # self.response_processor.process_historical_data_end(reqId, start, end)
        self.request_manager.process_data_end(reqId, start, end)

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
        super().fundamentalData(reqId, '')
        self.request_manager.process_data(reqId, data)
        # [request.process_data(data)
        #     for request in self.requests
        #     if request.request_id == reqId]

    # ! [fundamentaldata]

    # ! [error]
    @tracer.wrap(name='error from ewrapper', service='historical req')
    def error(self, reqId: TickerId, errorCode: int, errorString: str):
        span = tracer.current_span()
        span.set_tag('reqId', reqId)
        super().error(reqId, errorCode, errorString)

        if reqId == -1:
            # resets requests after errors
            self.notify_requests()
        try:
            self.request_manager.process_error(reqId, errorCode, errorString)
        except Exception as e:
            print('exception processing error - ewrapper impl line 162')
            print(e)

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

    def securityDefinitionOptionParameter(self, reqId: int, exchange: str,
                                          underlyingConId: int, tradingClass: str, multiplier: str,
                                          expirations: SetOfString, strikes: SetOfFloat):
        print(datetime.datetime.now(), reqId, exchange, underlyingConId, tradingClass, multiplier, expirations, strikes)
        self.request_manager.process_data(reqId, exchange, underlyingConId, tradingClass, multiplier, expirations,
                                          strikes)

    def securityDefinitionOptionParameterEnd(self, reqId: int):
        super().securityDefinitionOptionParameter(reqId)
        self.request_manager.process_data_end(reqId)
