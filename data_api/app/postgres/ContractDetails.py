from app import db
from app.exceptions import ValidationError
import sqlalchemy


class ContractDetails(db.Model):

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