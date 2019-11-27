import sqlalchemy

from data.sqlalchemy_base import SqlAlchemyBase

from proto.historical_data_pb2 import BarData as BarDataProto


class HistoricalData(SqlAlchemyBase):
    __tablename__ = "historical_data"

    symbol = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    secType = sqlalchemy.Column(sqlalchemy.String)
    exchange = sqlalchemy.Column(sqlalchemy.String)
    currency = sqlalchemy.Column(sqlalchemy.String)
    barSize = sqlalchemy.Column(sqlalchemy.String)
    whatToShow = sqlalchemy.Column(sqlalchemy.String)
    useRTH = sqlalchemy.Column(sqlalchemy.Integer)
    date = sqlalchemy.Column(sqlalchemy.Date, primary_key=True, nullable=False)
    open = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    high = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    low = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    close = sqlalchemy.Column(sqlalchemy.Float, nullable=False)
    volume = sqlalchemy.Column(sqlalchemy.Integer)
    barCount = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    average = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    __table_args__ = (
        sqlalchemy.Index('historical_data_symbol_date', symbol, date.desc()),
    )

    @staticmethod
    def from_json(json_bar_data):
        # body = json_contract.get('body')
        # try:
        return HistoricalData(**json_bar_data)
        # except:
        #     raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_bar_data = {
            'symbol': self.symbol,
            'secType': self.secType,
            'exchange': self.exchange,
            'currency': self.currency,
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

    def to_proto(self):
        return BarDataProto(date=self.date,
                            open=self.open,
                            high=self.high,
                            close=self.close,
                            volume=self.volume,
                            barCount=self.barCount,
                            average=self.average)
