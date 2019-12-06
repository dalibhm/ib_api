import random

# noinspection PyPackageRequirements
# from dateutil.parser import parse
from datetime import datetime

from sqlalchemy.orm import load_only
from sqlalchemy import and_

from data.db_factory import DbSessionFactory
from data.bar_data import HistoricalData
from data.head_timestamp import HeadTimestamp


class Repository:

    @classmethod
    def get_all_stocks(cls, limit=None):
        session = DbSessionFactory.create_session()

        query = session.query(HistoricalData.symbol).distinct()

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        session.close()

        return stocks

    @classmethod
    def get_latest_date(cls, symbol, date_format):
        session = DbSessionFactory.create_session()
        result = session.query(HistoricalData.date).filter(HistoricalData.symbol == symbol)\
            .order_by(HistoricalData.date.desc())\
            .first()
        session.close()

        return datetime.strptime(result.date, "%Y%m%d").strftime(date_format)

    @classmethod
    def get_head_timestamp(cls, symbol):
        session = DbSessionFactory.create_session()
        date = session.query(HeadTimestamp).first()
        session.close()

        return date

    @classmethod
    def get_historical_data_for_stock(cls, stock_symbol, start_date=None, end_date=None, whatToShow=None):
        session = DbSessionFactory.create_session()

        # fields = ['date', 'open', 'high', 'low', 'close', 'volume', 'barCount', 'average']
        if not start_date:
            if not end_date:
                historical_data = session.query(HistoricalData).filter(HistoricalData.symbol == stock_symbol).all()
            else:
                historical_data = session.query(HistoricalData).filter(HistoricalData.symbol == stock_symbol). \
                    filter(HistoricalData.date <= end_date).all()
        elif not end_date:
            historical_data = session.query(HistoricalData).filter(HistoricalData.symbol == stock_symbol). \
                filter(HistoricalData.date >= start_date).all()
        else:
            historical_data = session.query(HistoricalData).filter(HistoricalData.symbol == stock_symbol). \
                filter(and_(HistoricalData.date <= end_date, HistoricalData.date >= start_date)).all()

        session.close()

        return historical_data

    # @classmethod
    # def historical_data_for_stocks_in_period(cls, stock_list, start_date, end_date):
    #     session = DbSessionFactory.create_session()
    #
    #     historical_data = session.query(BarData).filter(BarData.symbol.in_(stock_list)). \
    #         filter(and_(BarData.date <= end_date, BarData.date >= start_date)).all()
    #
    #     session.close()
    #
    #     return historical_data

    # @classmethod
    # def historical_data_for_stock_in_period(cls, stock_symbol, start_date, end_date, whatToShow=None):
    #     session = DbSessionFactory.create_session()
    #
    #     historical_data = session.query(BarData).filter(BarData.symbol == stock_symbol). \
    #         filter(and_(BarData.date <= end_date, BarData.date >= start_date)).all()
    #
    #     session.close()
    #
    #     return historical_data

    @classmethod
    def add_historical_data(cls, historical_data):
        """
        Will not be used as data will sink from Kafka to Postgres
        Kafka postgres proved tricky, will write data here
        Finally, kafka is used. I will keep the method

        :param historical_data:
        :return: BarData
        """
        session = DbSessionFactory.create_session()

        db_data = HistoricalData(**historical_data)

        session.add(db_data)
        session.commit()

        return db_data
