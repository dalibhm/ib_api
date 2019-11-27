import random

# noinspection PyPackageRequirements
# from dateutil.parser import parse
from sqlalchemy import and_

from data.db_factory import DbSessionFactory
from data.bar_data import HistoricalData
from data.head_timestamp import HeadTimestamp

from data.stock import Stock


class Repository:

    @classmethod
    def get_all_stocks(cls, limit=None):
        session = DbSessionFactory.create_session()

        query = session.query(HistoricalData.symbol).distinct()
        session.close()

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        return stocks

    @classmethod
    def get_stock_by_id(cls, con_id):
        pass

    @classmethod
    def get_latest_date(cls, symbol):
        session = DbSessionFactory.create_session()
        symbol = session.query(HistoricalData.date).filter(HistoricalData.symbol == symbol).first()
        session.close()

        return symbol

    @classmethod
    def get_head_timestamp(cls, symbol):
        session = DbSessionFactory.create_session()
        stock = session.query(HeadTimestamp).first()
        session.close()

        return stock

    @classmethod
    def get_stock_(cls, stock):
        session = DbSessionFactory.create_session()

        db_stock = Stock(**stock)

        session.add(db_stock)
        session.commit()
        session.close()

        return db_stock

    @classmethod
    def get_all_exchanges(cls, limit=None):
        session = DbSessionFactory.create_session()

        query = session.query(Exchange)

        if limit:
            exchanges = query[:limit]
        else:
            exchanges = query.all()

        session.close()

        return exchanges

    @classmethod
    def get_exchange_by_code(cls, exchange_code):
        session = DbSessionFactory.create_session()

        stock = session.query(Exchange).filter(Exchange.code == exchange_code).first()

        session.close()

        return stock

    @classmethod
    def add_exchange(cls, exchange):
        session = DbSessionFactory.create_session()

        db_exchange = Exchange(**exchange)

        session.add(db_exchange)
        session.commit()

        return db_exchange
