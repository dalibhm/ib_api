import sqlalchemy

from app.exceptions import ValidationError
from app import db


class Contract(db.Model):
    __tablename__ = "contracts"

    conId = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    symbol = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    secType = sqlalchemy.Column(sqlalchemy.String, index=True, nullable=False)
    lastTradeDateOrContractMonth = sqlalchemy.Column(sqlalchemy.String)
    strike = sqlalchemy.Column(sqlalchemy.Float)  # float !!
    right = sqlalchemy.Column(sqlalchemy.String)
    multiplier = sqlalchemy.Column(sqlalchemy.String)
    exchange = sqlalchemy.Column(sqlalchemy.String, index=True)
    primaryExchange = sqlalchemy.Column(sqlalchemy.String, index=True)
    currency = sqlalchemy.Column(sqlalchemy.String, index=True)
    derivativeSecTypes = sqlalchemy.Column(sqlalchemy.String, index=True)
    localSymbol = sqlalchemy.Column(sqlalchemy.String)
    tradingClass = sqlalchemy.Column(sqlalchemy.String)
    includeExpired = sqlalchemy.Column(sqlalchemy.Boolean)
    secIdType = sqlalchemy.Column(sqlalchemy.String)  # CUSIP;SEDOL;ISIN;RIC
    secId = sqlalchemy.Column(sqlalchemy.String)

    comboLegsDescrip = sqlalchemy.Column(sqlalchemy.String)  # type: str
    comboLegs = sqlalchemy.Column(sqlalchemy.String)  # None  # type: list<ComboLeg>
    deltaNeutralContract = sqlalchemy.Column(sqlalchemy.String)  # None

    @staticmethod
    def from_json(json_contract):
        # body = json_contract.get('body')
        try:
            return Contract(**json_contract)
        except:
            raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_contract = {
            'conId': self.conId,
            'symbol': self.symbol,
            'secType': self.secType,
            'exchange': self.exchange,
            'primaryExchange': self.primaryExchange,
            'currency': self.currency,
            'secIdType': self.secIdType,
            'secId': self.secId
        }
        return json_contract
