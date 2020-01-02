from datetime import datetime

import sqlalchemy
from proto.contract_details_pb2 import ContractDetails as ProtoContractDetails
from data.sqlalchemy_base import SqlAlchemyBase


class ValidationError(Exception):
    pass


class ContractDetails(SqlAlchemyBase):

    __tablename__ = "contract_details"
    
    contractId = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    marketName = sqlalchemy.Column(sqlalchemy.String)
    minTick = sqlalchemy.Column(sqlalchemy.Float)
    orderTypes = sqlalchemy.Column(sqlalchemy.String)
    validExchanges = sqlalchemy.Column(sqlalchemy.String)
    priceMagnifier = sqlalchemy.Column(sqlalchemy.Integer)
    underConId = sqlalchemy.Column(sqlalchemy.Integer)
    longName = sqlalchemy.Column(sqlalchemy.String)
    contractMonth = sqlalchemy.Column(sqlalchemy.String)
    industry = sqlalchemy.Column(sqlalchemy.String)
    category = sqlalchemy.Column(sqlalchemy.String)
    subcategory = sqlalchemy.Column(sqlalchemy.String)
    timeZoneId = sqlalchemy.Column(sqlalchemy.String)
    tradingHours = sqlalchemy.Column(sqlalchemy.String)
    liquidHours = sqlalchemy.Column(sqlalchemy.String)
    evRule = sqlalchemy.Column(sqlalchemy.String)
    evMultiplier = sqlalchemy.Column(sqlalchemy.Integer)
    mdSizeMultiplier = sqlalchemy.Column(sqlalchemy.Integer)
    aggGroup = sqlalchemy.Column(sqlalchemy.Integer)
    underSymbol = sqlalchemy.Column(sqlalchemy.String)
    underSecType = sqlalchemy.Column(sqlalchemy.String)
    marketRuleIds = sqlalchemy.Column(sqlalchemy.String)
    secIdList = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    realExpirationDate = sqlalchemy.Column(sqlalchemy.String)
    lastTradeTime = sqlalchemy.Column(sqlalchemy.String)
    # BOND values
    cusip = sqlalchemy.Column(sqlalchemy.String)
    ratings = sqlalchemy.Column(sqlalchemy.String)
    descAppend = sqlalchemy.Column(sqlalchemy.String)
    bondType = sqlalchemy.Column(sqlalchemy.String)
    couponType = sqlalchemy.Column(sqlalchemy.String)
    callable = sqlalchemy.Column(sqlalchemy.Boolean)
    putable = sqlalchemy.Column(sqlalchemy.Boolean)
    coupon = sqlalchemy.Column(sqlalchemy.Integer)
    convertible = sqlalchemy.Column(sqlalchemy.Boolean)
    maturity = sqlalchemy.Column(sqlalchemy.String)
    issueDate = sqlalchemy.Column(sqlalchemy.String)
    nextOptionDate = sqlalchemy.Column(sqlalchemy.String)
    nextOptionType = sqlalchemy.Column(sqlalchemy.String)
    nextOptionPartial = sqlalchemy.Column(sqlalchemy.Boolean)
    notes = sqlalchemy.Column(sqlalchemy.String)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)

    @staticmethod
    def from_json(json_contract_details):
        # body = json_contract.get('body')
        try:
            return ContractDetails(**json_contract_details)
        except:
            raise ValidationError('ContractDetails cannot be constructed')

    def to_json(self):
        json_contract_details = {
            'contractId': self.contractId,
            'marketName' : self.marketName,
            'minTick': self.minTick,
            'orderTypes': self.orderTypes,
            'validExchanges': self.validExchanges,
            'priceMagnifier': self.priceMagnifier,
            'underConId': self.underConId,
            'longName': self.longName,
            'contractMonth': self.contractMonth,
            'industry': self.industry,
            'category': self.category,
            'subcategory': self.subcategory,
            'timeZoneId': self.timeZoneId,
            'tradingHours': self.tradingHours,
            'liquidHours': self.liquidHours,
            'evRule': self.evRule,
            'evMultiplier': self.evMultiplier,
            'mdSizeMultiplier': self.mdSizeMultiplier,
            'aggGroup': self.aggGroup,
            'underSymbol': self.underSymbol,
            'underSecType': self.underSecType,
            'marketRuleIds': self.marketRuleIds,
            'secIdList': self.secIdList,
            'realExpirationDate': self.realExpirationDate,
            'lastTradeTime': self.lastTradeTime,
            'cusip': self.cusip,
            'ratings': self.ratings,
            'descAppend': self.descAppend,
            'bondType': self.bondType,
            'couponType': self.couponType,
            'callable': self.callable,
            'putable': self.putable,
            'coupon': self.coupon,
            'convertible': self.convertible,
            'maturity': self.maturity,
            'issueDate': self.issueDate,
            'nextOptionDate': self.nextOptionDate,
            'nextOptionType': self.nextOptionType,
            'nextOptionPartial': self.nextOptionPartial,
            'notes': self.notes
        }
        return json_contract_details

    def to_proto(self):
        pb = ProtoContractDetails()
        pb.contractId = self.contractId
        pb.marketName = self.marketName
        pb.minTick = self.minTick
        pb.orderTypes = self.orderTypes
        pb.validExchanges = self.validExchanges
        pb.priceMagnifier = self.priceMagnifier
        pb.underConId = self.underConId
        pb.longName = self.longName
        pb.contractMonth = self.contractMonth
        pb.industry = self.industry
        pb.category = self.category
        pb.subcategory = self.subcategory
        pb.timeZoneId = self.timeZoneId
        pb.tradingHours = self.tradingHours
        pb.liquidHours = self.liquidHours
        pb.evRule = self.evRule
        pb.evMultiplier = self.evMultiplier
        pb.mdSizeMultiplier = self.mdSizeMultiplier
        pb.aggGroup = self.aggGroup
        pb.underSymbol = self.underSymbol
        pb.underSecType = self.underSecType
        pb.marketRuleIds = self.marketRuleIds
        pb.secIdList = self.secIdList
        pb.realExpirationDate = self.realExpirationDate
        pb.lastTradeTime = self.lastTradeTime
        pb.cusip = self.cusip
        pb.ratings = self.ratings
        pb.descAppend = self.descAppend
        pb.bondType = self.bondType
        pb.couponType = self.couponType
        pb.callable = self.callable
        pb.putable = self.putable
        pb.coupon = self.coupon
        pb.convertible = self.convertible
        pb.maturity = self.maturity
        pb.issueDate = self.issueDate
        pb.nextOptionDate = self.nextOptionDate
        pb.nextOptionType = self.nextOptionType
        pb.nextOptionPartial = self.nextOptionPartial
        pb.notes = self.notes
        return pb

    @staticmethod
    def from_proto(contract_details: ProtoContractDetails):
        result = ContractDetails()
        result.contractId = contract_details.contractId
        result.marketName = contract_details.marketName
        result.minTick = contract_details.minTick
        result.orderTypes = contract_details.orderTypes
        result.validExchanges = contract_details.validExchanges
        result.priceMagnifier = contract_details.priceMagnifier
        result.underConId = contract_details.underConId
        result.longName = contract_details.longName
        result.contractMonth = contract_details.contractMonth
        result.industry = contract_details.industry
        result.category = contract_details.category
        result.subcategory = contract_details.subcategory
        result.timeZoneId = contract_details.timeZoneId
        result.tradingHours = contract_details.tradingHours
        result.liquidHours = contract_details.liquidHours
        result.evRule = contract_details.evRule
        result.evMultiplier = contract_details.evMultiplier
        result.mdSizeMultiplier = contract_details.mdSizeMultiplier
        result.aggGroup = contract_details.aggGroup
        result.underSymbol = contract_details.underSymbol
        result.underSecType = contract_details.underSecType
        result.marketRuleIds = contract_details.marketRuleIds
        result.secIdList = contract_details.secIdList
        result.realExpirationDate = contract_details.realExpirationDate
        result.lastTradeTime = contract_details.lastTradeTime
        result.cusip = contract_details.cusip
        result.ratings = contract_details.ratings
        result.descAppend = contract_details.descAppend
        result.bondType = contract_details.bondType
        result.couponType = contract_details.couponType
        result.callable = contract_details.callable
        result.putable = contract_details.putable
        result.coupon = contract_details.coupon
        result.convertible = contract_details.convertible
        result.maturity = contract_details.maturity
        result.issueDate = contract_details.issueDate
        result.nextOptionDate = contract_details.nextOptionDate
        result.nextOptionType = contract_details.nextOptionType
        result.nextOptionPartial = contract_details.nextOptionPartial
        result.notes = contract_details.notes
        return result