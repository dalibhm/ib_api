from data.bar_data import HistoricalData
from data.db_factory import DbSessionFactory

symbol = 'SHOP'
DbSessionFactory.global_init()

session = DbSessionFactory.create_session()

result = session.query(HistoricalData.date).filter(HistoricalData.symbol == symbol)\
    .order_by(HistoricalData.date.desc())\
    .first()

session.close()