import random

import sqlalchemy
from sqlalchemy import and_

from data.db_factory import DbSessionFactory
from data.exchange import Exchange
from data.sqlalchemy_base import SqlAlchemyBase

from data.stock import Stock


class Repository:

    __session_factory = None

    @classmethod
    def init(cls, config):
        conn_string = 'postgresql://{}:{}@{}:{}/{}'.format(config.get('postgres', 'user'),
                                                           config.get('postgres', 'password'),
                                                           config.get('postgres', 'host'),
                                                           config.get('postgres', 'port'),
                                                           config.get('postgres', 'db'))

        print("[ Connecting to database : {} ]".format(conn_string))
        engine = sqlalchemy.create_engine(conn_string, echo=config.getboolean('postgres', 'echo'))

        SqlAlchemyBase.metadata.create_all(engine)

        cls.__session_factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @classmethod
    def get_all_stocks(cls, limit=None):
        # session = DbSessionFactory.create_session()
        session = cls.__session_factory()

        query = session.query(Stock)

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        session.close()

        return stocks

    @classmethod
    def get_stocks_in_exchange(cls, exchange_code, limit=None):
        """
        One stock can be present in multiple exchanges.

        :param exchange_code: exchange to check stocks in
        :param limit: maximum number of stocks to retrieve
        :return: list of rows in the exchange
        """
        session = cls.__session_factory()

        query = session.query(Stock).filter(Stock.exchange == exchange_code)

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        session.close()

        return stocks

    @classmethod
    def get_stock_by_id(cls, con_id):
        session = cls.__session_factory()

        stock = session.query(Stock).filter(Stock.con_id == con_id).first()

        session.close()

        return stock

    @classmethod
    def get_stock_by_id_and_exchange(cls, con_id, exchange):
        session = cls.__session_factory()

        stock = session.query(Stock).filter(and_(Stock.con_id == con_id,
                                                 Stock.exchange == exchange)).first()

        session.close()

        return stock

    @classmethod
    def get_stock_by_symbol(cls, stock_symbol):
        """
        THis method returns arbitrary the first row containing the stock.
        => remove the method and replace it with get_stock_by_symbol_and_exchange

        :param stock_symbol:
        :return:
        """
        session = cls.__session_factory()

        stock = session.query(Stock).filter(Stock.symbol == stock_symbol).first()

        session.close()

        return stock

    @classmethod
    def add_stock(cls, stock):
        session = cls.__session_factory()

        db_stock = Stock(**stock)

        query = session.query(Stock.symbol)
        if query:
            return
        session.add(db_stock)
        session.commit()

        return db_stock

    @classmethod
    def get_all_exchanges(cls, limit=None):
        session = cls.__session_factory()

        query = session.query(Exchange)

        if limit:
            exchanges = query[:limit]
        else:
            exchanges = query.all()

        session.close()

        return exchanges

    @classmethod
    def get_exchange_by_code(cls, exchange_code):
        session = cls.__session_factory()

        stock = session.query(Exchange).filter(Exchange.code == exchange_code).first()

        session.close()

        return stock

    @classmethod
    def add_exchange(cls, exchange):
        session = cls.__session_factory()

        existing_exchange = session.query(Exchange).filter(Exchange.code == exchange['code']).first()
        if existing_exchange:
            return

        db_exchange = Exchange(**exchange)
        session.add(db_exchange)
        # session.commit()
        session.close()

        return db_exchange
