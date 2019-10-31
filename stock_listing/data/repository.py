import random

# noinspection PyPackageRequirements
# from dateutil.parser import parse

from data.db_factory import DbSessionFactory
from data.exchange import Exchange

from data.stock import Stock


class Repository:

    @classmethod
    def get_all_stocks(cls, limit=None):
        session = DbSessionFactory.create_session()

        query = session.query(Stock)

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        session.close()

        return stocks

    @classmethod
    def get_stocks_in_exchange(cls, exchange_code, limit=None):
        session = DbSessionFactory.create_session()

        query = session.query(Stock).filter(Stock.exchange == exchange_code)

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        session.close()

        return stocks

    @classmethod
    def get_stock_by_id(cls, con_id):
        session = DbSessionFactory.create_session()

        stock = session.query(Stock).filter(Stock.con_id == con_id).first()

        session.close()

        return stock

    @classmethod
    def get_stock_by_symbol(cls, stock_symbol):
        session = DbSessionFactory.create_session()

        stock = session.query(Stock).filter(Stock.symbol == stock_symbol).first()

        session.close()

        return stock

    @classmethod
    def add_stock(cls, stock):
        session = DbSessionFactory.create_session()

        db_stock = Stock(**stock)

        session.add(db_stock)
        session.commit()

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
