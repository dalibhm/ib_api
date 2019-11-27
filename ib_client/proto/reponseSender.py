from __future__ import print_function
from ibapi import Contract as ib_contract

import grpc_service

import proto.response_data_pb2 as rd
import proto.response_data_pb2_grpc as rd_grpc


class ResponseSender:
    def __init__(self):
        channel = grpc_service.insecure_channel('localhost:50051')
        self.stub = rd_grpc.RequestDataStub(channel)

    @staticmethod
    def set_contract(contract: ib_contract):
        _contract = rd.Contract(conId=contract.conId,
                                symbol=contract.symbol,
                                secType=contract.secType,
                                exchange=contract.exchange,
                                primaryExchange=contract.primaryExchange,
                                currency=contract.currency)
        return _contract

#     def send_contractDetails(self,
#                             request_id,
#                             contract: ib_contract,
#                             contract_details: ib_contract_details):
#         message = rd.HistoricalDataResponse(
#             requestId=request_id,
#             contract = ResponseSender.set_contract(contract),
#             marketName=contract_details.marketName,
#             minTick = contract_details.minTick,
#         string orderTypes = 4;
#         string validExchanges = 5;
#         int32 priceMagnifier = 6;
#         int32 underConId = 7;
#         string longName = 8;
#         string contractMonth = 9;
#         string industry = 10;
#         string category = 13;
#         string subcategory = 14;
#         string timeZoneId = 15;
#         string tradingHours = 16;
#         string liquidHours = 17;
#         string evRule = 18;
#         int32 evMultiplier = 19;
#         int32 mdSizeMultiplier = 20;
#         int32 aggGroup = 21;
#         string underSymbol = 22;
#         string underSecType = 23;
#         string marketRuleIds = 24;
# //
# //        TO COMPLETE LATER ONCE I KNOW WHAT IT IS
# //
# //        secIdList = None
#
#         string realExpirationDate = 25;
#         string lastTradeTime = 26;
#
# //        # BOND values
#         string cusip = 27;
#         string ratings = 28;
#         string descAppend = 29;
#         string bondType = 30;
#         string couponType = 31;
#         bool callable = 32;
#         bool putable = 33;
#         int32 coupon = 34;
#         bool convertible = 35;
#         string maturity = 36;
#         string issueDate = 37;
#         string nextOptionDate = 38;
#         string nextOptionType = 39;
#         string nextOptionPartial = 40;
#         string notes = 41;)
#         response = self.stub.SendHistoricalData(message)
#         print("Historical data successfully sent: " + str(response.message))

    def send_historical_data(self, request_id, contract, xml_string):
        message = rd.HistoricalDataResponse(
            requestId=request_id,
            contract=ResponseSender.set_contract(contract),
            xml=xml_string)
        response = self.stub.SendHistoricalData(message)
        print("Historical data successfully sent: " + str(response.message))

    def send_fundamental_data(self, request_id, contract, xml_string):
        message = rd.fundamentalDataResponse(
            requestId=request_id,
            contract=ResponseSender.set_contract(contract),
            xml=xml_string)
        response = self.stub.SendFundamentalData(message)
        print("Testbed client received Historical data: " + str(response.message))


