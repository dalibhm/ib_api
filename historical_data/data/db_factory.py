import os
from configparser import ConfigParser

import sqlalchemy
import sqlalchemy.orm

from data.sqlalchemy_base import SqlAlchemyBase


class DbSessionFactory:
    __session_factory = None

    @classmethod
    def global_init(cls):
        config = ConfigParser()
        config.read(os.path.join('..', 'settings', 'development.ini'))
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
    def create_session(cls):
        return cls.__session_factory()
