import random

# noinspection PyPackageRequirements
# from dateutil.parser import parse
from datetime import datetime

import sqlalchemy
from sqlalchemy.orm import load_only
from sqlalchemy import and_

from data.option_params import OptionParams
from data.sqlalchemy_base import SqlAlchemyBase


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
    def get_option_params(cls, con_id, limit=None):
        session = cls.__session_factory()

        query = session.query(OptionParams).filter(OptionParams.underlyingConId == con_id)

        if limit:
            stocks = query[:limit]
        else:
            stocks = query.all()

        session.close()

        return stocks

    @classmethod
    def add_option_params(cls, option_params: OptionParams):
        """
        Will not be used as data will sink from Kafka to Postgres
        Kafka postgres proved tricky, will write data here
        Finally, kafka is used. I will keep the method

        :param option_params:
        :return: None
        """
        session = cls.__session_factory()

        query = session.query(OptionParams) \
            .filter(and_(OptionParams.underlyingConId == option_params.underlyingConId,
                         OptionParams.exchange == option_params.exchange)
                    ) \
            .order_by(OptionParams.insert_date.desc()) \
            .first()

        if query:
            if set(query.strikes) == set(option_params.strikes) \
                    and set(query.expirations) == set(option_params.expirations):
                return

        session.add(option_params)
        session.commit()
