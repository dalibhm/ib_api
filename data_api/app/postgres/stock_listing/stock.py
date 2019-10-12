import sqlalchemy

from app import db
from app.exceptions import ValidationError


class Stock(db.Model):
    __tablename__ = "stocks"

    con_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    # add statement info id reference
    ib_symbol = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    currency = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    symbol = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    exchange = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    product_description_link = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    @staticmethod
    def from_json(json_stock):
        try:
            return Stock(**json_stock)
        except:
            raise ValidationError('Contract cannot be constructed')

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
