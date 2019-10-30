import datetime
import logging

from ibapi.common import BarData, ListOfHistoricalTick, ListOfHistoricalTickBidAsk, TickerId, ListOfHistoricalTickLast, \
    OrderId
from ibapi.contract import ContractDetails, Contract
from ibapi.order import Order
from ibapi.order_state import OrderState
from ibapi.wrapper import EWrapper

from ib_response_manager.grpc_reponse_manager import GrpcResponseManager
from ib_response_manager.response_processor_factory import ResponseProcessorFactory

logger = logging.getLogger()


class EWrapperImpl(EWrapper):
    def __init__(self, config, request_manager):
        super().__init__()
        self.asynchronous = False
        self.request_manager = request_manager
        self.response_processor = ResponseProcessorFactory(config).create()
        self.response_manager = GrpcResponseManager(config.get('data api', 'fundamental_data_server'))

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
        print("HistoricalData. ReqId:", reqId, "BarData.", bar)
        request = self.request_manager.get_request_by_id(reqId)
        self.response_processor.process_historical_data(request, bar)

    # ! [historicaldata]

    # ! [historicaldataend]
    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)

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
        print('from fundamental data')
        super().fundamentalData(reqId, data)
        request = self.request_manager.get_request_by_id(reqId)
        self.response_manager.process_financial_data(request, data)

    # ! [fundamentaldata]

    # ! [error]
    def error(self, reqId: TickerId, errorCode: int, errorString: str):
        super().error(reqId, errorCode, errorString)
        print("Error. Id:", reqId, "Code:", errorCode, "Msg:", errorString)

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
