from app.exceptions import ValidationError
import sqlalchemy
from app import db


class BarData(db.Model):
    __tablename__ = "historical_data"

    symbol = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    secType = sqlalchemy.Column(sqlalchemy.String)
    exchange = sqlalchemy.Column(sqlalchemy.String)
    currency = sqlalchemy.Column(sqlalchemy.String)
    endDateTime = sqlalchemy.Column(sqlalchemy.String)
    duration = sqlalchemy.Column(sqlalchemy.String)
    barSize = sqlalchemy.Column(sqlalchemy.String)
    whatToShow = sqlalchemy.Column(sqlalchemy.String)
    useRTH = sqlalchemy.Column(sqlalchemy.Integer)
    date = sqlalchemy.Column(sqlalchemy.String, primary_key=True, nullable=False)
    open = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    high = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    low = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    close = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    volume = sqlalchemy.Column(sqlalchemy.Integer)
    barCount = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    average = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    @staticmethod
    def from_json(json_bar_data):
        # body = json_contract.get('body')
        try:
            return BarData(**json_bar_data)
        except:
            raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_bar_data = {
            'symbol': self.symbol,
            'secType': self.secType,
            'exchange': self.exchange,
            'currency': self.currency,
            'endDateTime': self.endDateTime,
            'duration': self.duration,
            'barSize': self.barSize,
            'whatToShow': self.whatToShow,
            'useRTH': self.useRTH,
            'date': self.date,
            'open': self.open,
            'high': self.high,
            'close': self.close,
            'volume': self.volume,
            'barCount': self.barCount,
            'average': self.average
        }
        return json_bar_data