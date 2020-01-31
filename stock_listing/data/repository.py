import random
from configparser import ConfigParser

import sqlalchemy
from injector import inject
from sqlalchemy import and_

from data.db_factory import DbSessionFactory
from data.exchange import Exchange
from data.sqlalchemy_base import SqlAlchemyBase

from data.stock import Stock


class Repository:
    @inject
    def __init__(self, config: ConfigParser):
        conn_string = 'postgresql://{}:{}@{}:{}/{}'.format(config.get('postgres', 'user'),
                                                           config.get('postgres', 'password'),
                                                           config.get('postgres', 'host'),
                                                           config.get('postgres', 'port'),
                                                           config.get('postgres', 'db'))

        print("[ Connecting to database : {} ]".format(conn_string))
        engine = sqlalchemy.create_engine(conn_string, echo=config.getboolean('postgres', 'echo'))

        SqlAlchemyBase.metadata.create_all(engine)

        self.__session_factory = sqlalchemy.orm.sessionmaker(bind=engine)

    def get_all_stocks(self, limit=None):
        # session = DbSessionFactory.create_session()
        session = self.__session_factory()

        query = session.query(Stock)

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        session.close()

        return stocks

    def get_stocks_in_exchange(self, exchange_code, limit=None):
        """
        One stock can be present in multiple exchanges.

        :param exchange_code: exchange to check stocks in
        :param limit: maximum number of stocks to retrieve
        :return: list of rows in the exchange
        """
        session = self.__session_factory()

        query = session.query(Stock).filter(Stock.exchange == exchange_code)

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        session.close()

        return stocks

    def get_stock_by_id(self, con_id):
        session = self.__session_factory()

        stock = session.query(Stock).filter(Stock.con_id == con_id).first()

        session.close()

        return stock

    def get_stock_by_id_and_exchange(self, con_id, exchange):
        session = self.__session_factory()

        stock = session.query(Stock).filter(and_(Stock.con_id == con_id,
                                                 Stock.exchange == exchange)).first()

        session.close()

        return stock

    def get_stock_by_symbol(self, stock_symbol):
        """
        THis method returns arbitrary the first row containing the stock.
        => remove the method and replace it with get_stock_by_symbol_and_exchange

        :param stock_symbol:
        :return:
        """
        session = self.__session_factory()

        stock = session.query(Stock).filter(Stock.symbol == stock_symbol).first()

        session.close()

        return stock

    def add_stock(self, stock):
        session = self.__session_factory()

        query = session.query(Stock).filter(and_(Stock.symbol == stock['symbol'], Stock.exchange == stock['exchange'])).first()
        if query:
            session.close()
            return

        db_stock = Stock(**stock)
        session.add(db_stock)
        session.commit()
        session.close()

        return db_stock

    def get_all_exchanges(self, limit=None):
        session = self.__session_factory()

        query = session.query(Exchange)

        if limit:
            exchanges = query[:limit]
        else:
            exchanges = query.all()

        session.close()

        return exchanges

    def get_exchange_by_code(self, exchange_code):
        session = self.__session_factory()

        stock = session.query(Exchange).filter(Exchange.code == exchange_code).first()

        session.close()

        return stock

    def add_exchange(self, exchange):
        session = self.__session_factory()

        existing_exchange = session.query(Exchange).filter(Exchange.code == exchange['code']).first()
        if existing_exchange:
            session.close()
            return

        db_exchange = Exchange(**exchange)
        session.add(db_exchange)
        session.commit()
        session.close()

        return db_exchange
