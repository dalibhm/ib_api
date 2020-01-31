from datetime import datetime

import sqlalchemy

from data.sqlalchemy_base import SqlAlchemyBase

from proto.option_params_pb2 import OptionParams as OptionParamsProto


class OptionParams(SqlAlchemyBase):
    __tablename__ = "options_params"

    exchange = sqlalchemy.Column(sqlalchemy.String, primary_key=True, nullable=False)
    underlyingConId = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    tradingClass = sqlalchemy.Column(sqlalchemy.String)
    multiplier = sqlalchemy.Column(sqlalchemy.Integer)
    expirations = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.String))
    strikes = sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.FLOAT))
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.now, primary_key=True)

    __table_args__ = (
        sqlalchemy.Index('option_params_underlying', underlyingConId),
        sqlalchemy.Index('option_params_exchange', exchange),
        sqlalchemy.Index('option_params_exchange_underlying', exchange, underlyingConId),
    )

    def to_json(self):
        json_option_params = {
            'exchange': self.exchange,
            'underlyingConId': self.underlyingConId,
            'tradingClass': self.tradingClass,
            'multiplier': self.multiplier,
            'expirations': self.expirations,
            'strikes': self.strikes
        }
        return json_option_params

    def to_proto(self):
        pb = OptionParamsProto()
        pb.exchange = self.exchange
        pb.underlyingConId = self.underlyingConId
        pb.tradingClass = self.tradingClass
        pb.multiplier = self.multiplier
        pb.expirations.extend(self.expirations)
        pb.strikes.extend(self.strikes)
        return pb

    @staticmethod
    def from_proto(option_params: OptionParamsProto):
        result = OptionParams(exchange=option_params.exchange,
                              underlyingConId=option_params.underlyingConId,
                              tradingClass=option_params.tradingClass,
                              multiplier=option_params.multiplier,
                              expirations=option_params.expirations,
                              strikes=option_params.strikes)
        return result
