# ! [socket_init]
import collections
import datetime
import logging

from ibapi.common import TickerId, OrderId, BarData, ListOfHistoricalTickBidAsk, ListOfHistoricalTickLast, ListOfHistoricalTick
from ibapi.contract import Contract, ContractDetails
from ibapi.object_implem import Object
from ibapi.order import Order
from ibapi.order_state import OrderState
from ibapi.utils import iswrapper

from data_api_client.api_client import DataApiClient
from requestmanager.requestmanager import RequestManager

from ib_client import TestClient
from ib_wrapper import TestWrapper


def printWhenExecuting(fn):
    def fn2(self):
        print("   doing", fn.__name__)
        fn(self)
        print("   done w/", fn.__name__)

    return fn2


def printinstance(inst: Object):
    attrs = vars(inst)
    print(', '.join("%s: %s" % item for item in attrs.items()))


class Activity(Object):
    def __init__(self, reqMsgId, ansMsgId, ansEndMsgId, reqId):
        self.reqMsdId = reqMsgId
        self.ansMsgId = ansMsgId
        self.ansEndMsgId = ansEndMsgId
        self.reqId = reqId


class RequestMgr(Object):
    def __init__(self):
        # I will keep this simple even if slower for now: only one list of
        # requests finding will be done by linear search
        self.requests = []

    def addReq(self, req):
        self.requests.append(req)

    def receivedMsg(self, msg):
        pass


logger = logging.getLogger()


class TestApp(TestWrapper, TestClient):
    request_manager: RequestManager

    def __init__(self):
        TestWrapper.__init__(self)
        TestClient.__init__(self, wrapper=self)
        # ! [socket_init]
        self.nKeybInt = 0
        self.started = False
        self.nextValidOrderId = None
        self.permId2ord = {}
        self.reqId2nErr = collections.defaultdict(int)
        self.globalCancelOnly = False
        self.simplePlaceOid = None
        self.request_manager = RequestManager()
        self.data_api_client = DataApiClient()

    def dumpTestCoverageSituation(self):
        for clntMeth in sorted(self.clntMeth2callCount.keys()):
            logger.debug("ClntMeth: %-30s %6d" % (clntMeth,
                                                  self.clntMeth2callCount[clntMeth]))

        for wrapMeth in sorted(self.wrapMeth2callCount.keys()):
            logger.debug("WrapMeth: %-30s %6d" % (wrapMeth,
                                                  self.wrapMeth2callCount[wrapMeth]))

    def dumpReqAnsErrSituation(self):
        logger.debug("%s\t%s\t%s\t%s" % ("ReqId", "#Req", "#Ans", "#Err"))
        for reqId in sorted(self.reqId2nReq.keys()):
            nReq = self.reqId2nReq.get(reqId, 0)
            nAns = self.reqId2nAns.get(reqId, 0)
            nErr = self.reqId2nErr.get(reqId, 0)
            logger.debug("%d\t%d\t%s\t%d" % (reqId, nReq, nAns, nErr))

    @iswrapper
    # ! [connectack]
    def connectAck(self):
        if self.asynchronous:
            self.startApi()

    # ! [connectack]

    @iswrapper
    # ! [nextvalidid]
    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)

        logger.debug("setting nextValidOrderId: %d", orderId)
        self.nextValidOrderId = orderId
        print("NextValidId:", orderId)
        # ! [nextvalidid]

        # we can start now
        # self.start()

    def start(self):
        if self.started:
            return

        self.started = True

        if self.globalCancelOnly:
            print("Executing GlobalCancel only")
            self.reqGlobalCancel()

    def keyboardInterrupt(self):
        self.nKeybInt += 1
        if self.nKeybInt == 1:
            self.stop()
        else:
            print("Finishing test")
            self.done = True

    def stop(self):
        print("Executing cancels")
        # put something here to cancel issued orders
        print("Executing cancels ... finished")

    def nextOrderId(self):
        oid = self.nextValidOrderId
        self.nextValidOrderId += 1
        return oid

    @iswrapper
    # ! [error]
    def error(self, reqId: TickerId, errorCode: int, errorString: str):
        super().error(reqId, errorCode, errorString)
        print("Error. Id:", reqId, "Code:", errorCode, "Msg:", errorString)

    # ! [error] self.reqId2nErr[reqId] += 1

    @iswrapper
    def winError(self, text: str, lastError: int):
        super().winError(text, lastError)

    @iswrapper
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

    @iswrapper
    # ! [openorderend]
    def openOrderEnd(self):
        super().openOrderEnd()
        print("OpenOrderEnd")

        logger.debug("Received %d openOrders", len(self.permId2ord))

    # ! [openorderend]

    @iswrapper
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

    @printWhenExecuting
    def historicalDataOperations_req(self):
        pass
        # Requesting historical data
        # ! [reqHeadTimeStamp]
        # self.reqHeadTimeStamp(4101, ContractSamples.USStockAtSmart(), "TRADES", 0, 1)
        # # ! [reqHeadTimeStamp]
        #
        # # ! [reqhistoricaldata]
        # queryTime = (datetime.datetime.today() - datetime.timedelta(days=180)).strftime("%Y%m%d %H:%M:%S")
        # self.reqHistoricalData(4102, ContractSamples.EurGbpFx(), queryTime,
        #                        "1 M", "1 day", "MIDPOINT", 1, 1, False, [])
        # self.reqHistoricalData(4103, ContractSamples.EuropeanStock(), queryTime,
        #                        "10 D", "1 min", "TRADES", 1, 1, False, [])
        # self.reqHistoricalData(4104, ContractSamples.EurGbpFx(), "",
        #                        "1 M", "1 day", "MIDPOINT", 1, 1, True, [])
        # ! [reqhistoricaldata]

    @printWhenExecuting
    def historicalDataOperations_cancel(self):
        # ! [cancelHeadTimestamp]
        self.cancelHeadTimeStamp(4101)
        # ! [cancelHeadTimestamp]

        # Canceling historical data requests
        # ! [cancelhistoricaldata]
        self.cancelHistoricalData(4102)
        self.cancelHistoricalData(4103)
        self.cancelHistoricalData(4104)
        # ! [cancelhistoricaldata]

    @printWhenExecuting
    def historicalTicksOperations(self):
        # ! [reqhistoricalticks]
        self.reqHistoricalTicks(18001, ContractSamples.USStockAtSmart(),
                                "20170712 21:39:33", "", 10, "TRADES", 1, True, [])
        self.reqHistoricalTicks(18002, ContractSamples.USStockAtSmart(),
                                "20170712 21:39:33", "", 10, "BID_ASK", 1, True, [])
        self.reqHistoricalTicks(18003, ContractSamples.USStockAtSmart(),
                                "20170712 21:39:33", "", 10, "MIDPOINT", 1, True, [])
        # ! [reqhistoricalticks]

    @iswrapper
    # ! [headTimestamp]
    def headTimestamp(self, reqId: int, headTimestamp: str):
        print("HeadTimestamp. ReqId:", reqId, "HeadTimeStamp:", headTimestamp)

    # ! [headTimestamp]

    def reqHistoricalData(self, reqId: TickerId, contract: Contract, endDateTime: str,
                          durationStr: str, barSizeSetting: str, whatToShow: str,
                          useRTH: int, formatDate: int, keepUpToDate: bool, chartOptions: list):
        # self.cache.register_data_request(request_id=reqId, type=DataType.Historical, contract=contract)
        super().reqHistoricalData(reqId, contract, endDateTime,
                                  durationStr, barSizeSetting, whatToShow,
                                  useRTH, formatDate, keepUpToDate, chartOptions)

    def reqFundamentalData(self, reqId: TickerId, contract: Contract,
                           reportType: str, fundamentalDataOptions: list):

        super().reqFundamentalData(reqId, contract, reportType, fundamentalDataOptions)

    @iswrapper
    # ! [currenttime]
    def currentTime(self, time: int):
        super().currentTime(time)
        print("CurrentTime:", datetime.datetime.fromtimestamp(time).strftime("%Y%m%d %H:%M:%S"))

    # ! [currenttime]

    @printWhenExecuting
    def matching_symbols_req(self):
        self.reqMatchingSymbols(201, "DAX")

    def contractDetails(self, reqId: int, contractDetails: ContractDetails):
        super().contractDetails(reqId, contractDetails)
        self.data_api_client.post_contract_details(contractDetails)


    # ! [contractdetails]

    @iswrapper
    # ! [contractdetailsend]
    def contractDetailsEnd(self, reqId: int):
        super().contractDetailsEnd(reqId)
        print("ContractDetailsEnd. ReqId:", reqId)

    # ! [contractdetailsend]

    # ! [historicaldata]
    def historicalData(self, reqId: int, bar: BarData):
        print("HistoricalData. ReqId:", reqId, "BarData.", bar)
        request = self.request_manager.get_request_by_id(reqId)
        self.data_api_client.post_historical_data(request, bar)

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
        super().fundamentalData(reqId, data)
        request = self.request_manager.get_request_by_id(reqId)
        self.data_api_client.post_financial_data(request, data)

    # ! [fundamentaldata]
