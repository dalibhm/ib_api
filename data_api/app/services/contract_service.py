from postgres.db_factory import DbSessionFactory
from postgres.__all_models import Contract, BarData, ContractDetails


def save_contract(contract: Contract):
    session = DbSessionFactory.create_session()
    res = session.query(Contract) \
        .filter(Contract.conId == contract.conId) \
        .first()
    if not res:
        try:
            db_contract = Contract(**contract.__dict__)
            session.add(db_contract)
            session.commit()
        except Exception as e:
            msg = 'Failed to write contract for conid: {}, symbol: {}' \
                .format(contract.conId, contract.symbol)
            self.logger.exception(msg)
            # self.session.rollback()
    session.close()


def save_historical_data(self, contract: Contract, bar_data: list):
    session = DbSessionFactory.create_session()
    for hist_data in bar_data:
        res = session.query(BarData) \
            .filter(and_(BarData.symbol == contract.symbol,
                         BarData.date == hist_data.date)) \
            .first()

        if res:
            continue
        else:
            obj_dict = hist_data.__dict__
            db_bar_data = BarData(**obj_dict)
            db_bar_data.symbol = contract.symbol
            session.add(db_bar_data)
            session.commit()
    session.close()


def save_historical_data_2(self, request, bar_data: list):
    session = DbSessionFactory.create_session()
    for hist_data in bar_data:
        res = session.query(BarData) \
            .filter(and_(BarData.symbol == request['symbol'],
                         BarData.date == hist_data.date)) \
            .first()

        if res:
            continue
        else:
            obj_dict = hist_data.__dict__
            db_bar_data = BarData(**obj_dict)
            db_bar_data.symbol = request['symbol']
            db_bar_data.secType = request['secType']
            db_bar_data.exchange = request['exchange']
            db_bar_data.currency = request['currency']
            db_bar_data.endDateTime = request['endDateTime']
            db_bar_data.duration = request['duration']
            db_bar_data.barSize = request['barSize']
            db_bar_data.whatToShow = request['whatToShow']
            db_bar_data.useRTH = request['useRTH']
            session.add(db_bar_data)
            session.commit()
    session.close()


def save_fundamental_data(self, xml_string: str):
    pass


def save_contract_details(self, contract_details: ContractDetails):
    session = DbSessionFactory.create_session()
    obj_dict = contract_details.__dict__
    contract = obj_dict.pop('contract')
    self.save_contract(contract)
    db_contract_details = ContractDetails(**obj_dict)
    db_contract_details.contractId = contract.conId
    res = session.query(ContractDetails) \
        .filter(ContractDetails.contractId == contract.conId) \
        .first()
    if not res:
        try:
            session.add(db_contract_details)
            session.commit()
            session.close()
        except Exception as e:
            msg = 'Failed to write contract details for conid: {}, symbol: {}' \
                .format(contract.conId, contract.symbol)
            self.logger.exception(msg)
    session.close()
