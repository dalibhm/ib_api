import random

# noinspection PyPackageRequirements
# from dateutil.parser import parse
from datetime import datetime

import sqlalchemy
from sqlalchemy.orm import load_only
from sqlalchemy import and_

from data.contract import Contract
from data.contract_details import ContractDetails
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
    def get_contract(cls, con_id: int) -> Contract:
        session = cls.__session_factory()

        query = session.query(Contract).filter(Contract.conId == con_id)

        if query:
           if len(query) > 1:
               session.close()
               raise ResourceWarning

        session.close()

        return query.first()

    @classmethod
    def add_contract(cls, contract: Contract) -> None:
        """
        Will not be used as data will sink from Kafka to Postgres
        Kafka postgres proved tricky, will write data here
        Finally, kafka is used. I will keep the method

        :param contract_details:
        :return: None
        """
        session = cls.__session_factory()

        query = session.query(ContractDetails) \
            .filter(Contract.conId == contract.conId) \
            .first()

        if query:
            return

        session.add(contract)
        session.commit()


    @classmethod
    def get_contract_details(cls, con_id: int) -> ContractDetails:
        session = cls.__session_factory()

        query = session.query(ContractDetails).filter(ContractDetails.contractId == con_id)

        if query:
           if len(query) > 1:
               session.close()
               raise ResourceWarning

        session.close()

        return query.first()

    @classmethod
    def add_contract_details(cls, contract_details: ContractDetails) -> None:
        """
        Will not be used as data will sink from Kafka to Postgres
        Kafka postgres proved tricky, will write data here
        Finally, kafka is used. I will keep the method

        :param contract_details:
        :return: None
        """
        session = cls.__session_factory()

        query = session.query(ContractDetails) \
            .filter(ContractDetails.contractId == contract_details.contractId) \
            .first()

        if query:
            return

        session.add(contract_details)
        session.commit()
