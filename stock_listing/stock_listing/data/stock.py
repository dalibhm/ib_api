from datetime import datetime

import sqlalchemy

from data.sqlalchemy_base import SqlAlchemyBase
from proto import listing_pb2


class Stock(SqlAlchemyBase):
    __tablename__ = "stocks"

    con_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    # add statement info id reference
    ib_symbol = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    currency = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    symbol = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    exchange = sqlalchemy.Column(sqlalchemy.String, nullable=False, primary_key=True)
    product_description_link = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.now)

    @staticmethod
    def from_json(json_stock):
        # try:
        return Stock(**json_stock)
        # except:
        #     raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_stock = {
            'con_id': self.con_id,
            'ib_symbol': self.ib_symbol,
            'currency': self.currency,
            'symbol': self.symbol,
            'exchange': self.exchange,
            'product_description_link': self.product_description_link
        }
        return json_stock

    def get_stock_listing(self):
        proto = listing_pb2.StockListing(conId=self.con_id,
                                         symbol=self.ib_symbol,
                                         currency=self.currency,
                                         exchange=self.exchange)
        return proto
