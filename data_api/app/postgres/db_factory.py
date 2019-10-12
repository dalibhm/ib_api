from configparser import ConfigParser

import sqlalchemy
import sqlalchemy.orm

from postgres.sqlalchemy_base import SqlAlchemyBase


class DbSessionFactory:
    factory = None

    @staticmethod
    def global_init(config: ConfigParser):
        if DbSessionFactory.factory:
            return
        connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(config.get('postgres', 'user'),
                                                                 config.get('postgres', 'password'),
                                                                 config.get('postgres', 'host'),
                                                                 config.get('postgres', 'port'),
                                                                 config.get('postgres', 'db')
                                                                 )
        engine = sqlalchemy.create_engine(connection_string, echo=config.getboolean('postgres', 'echo'))
        SqlAlchemyBase.metadata.create_all(engine)
        # DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine, autoflush=True)
        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @staticmethod
    def create_session() -> sqlalchemy.orm.Session:
        return DbSessionFactory.factory()
