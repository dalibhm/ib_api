import sqlalchemy

from data.sqlalchemy_base import SqlAlchemyBase
from proto.contract_pb2 import Contract as ProtoContract


class Contract(SqlAlchemyBase):
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

    def to_proto(self):
        pb = ProtoContract()
        pb.conId = self.conId
        pb.symbol = self.symbol
        pb.secType = self.secType
        pb.lastTradeDateOrContractMonth = self.lastTradeDateOrContractMonth
        pb.strike = self.strike
        pb.right = self.right
        pb.multiplier = self.multiplier
        pb.exchange = self.exchange
        pb.primaryExchange = self.primaryExchange
        pb.currency = self.currency
        pb.derivativeSecTypes = self.derivativeSecTypes
        pb.localSymbol = self.localSymbol
        pb.tradingClass = self.tradingClass
        pb.includeExpired = self.includeExpired
        pb.secIdType = self.secIdType
        pb.secId = self.secId
        pb.comboLegsDescrip = self.comboLegsDescrip
        pb.comboLegs = self.comboLegs
        pb.deltaNeutralContract = self.deltaNeutralContract
        
    @staticmethod
    def from_proto(contract: ProtoContract):
        result = Contract()
        result.conId = contract.conId
        result.symbol = contract.symbol
        result.secType = contract.secType
        result.lastTradeDateOrContractMonth = contract.lastTradeDateOrContractMonth
        result.strike = contract.strike
        result.right = contract.right
        result.multiplier = contract.multiplier
        result.exchange = contract.exchange
        result.primaryExchange = contract.primaryExchange
        result.currency = contract.currency
        result.derivativeSecTypes = contract.derivativeSecTypes
        result.localSymbol = contract.localSymbol
        result.tradingClass = contract.tradingClass
        result.includeExpired = contract.includeExpired
        result.secIdType = contract.secIdType
        result.secId = contract.secId
        result.comboLegsDescrip = contract.comboLegsDescrip
        result.comboLegs = contract.comboLegs
        result.deltaNeutralContract = contract.deltaNeutralContract
        return result