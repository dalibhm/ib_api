import sqlalchemy
import sqlalchemy.orm

from data.sqlalchemy_base import SqlAlchemyBase


class DbSessionFactory:
    __session_factory = None

    @classmethod
    def global_init(cls):
        conn_string = 'postgresql://ib_test:ib_test@localhost:5432/ib_test'

        # print("Connection string: " + conn_string)
        engine = sqlalchemy.create_engine(conn_string, echo=False)

        SqlAlchemyBase.metadata.create_all(engine)

        cls.__session_factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @classmethod
    def create_session(cls):
        return cls.__session_factory()
