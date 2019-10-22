import xml.etree.ElementTree as ET
from collections import namedtuple
from mongo_documents.FinancialReport.statement import Statement

AnnualFiscalPeriod = namedtuple('AnnualFiscalPeriod', ['Type', 'EndDate', 'FiscalYear'])
InterimFiscalPeriod = namedtuple('InterimFiscalPeriod', ['Type', 'EndDate', 'FiscalYear', 'FiscalPeriodNumber'])


def save_statements(period_type, root, ticker, last_modified):
    xml_tag = 'FinancialStatements/{}Periods'.format(period_type)
    _periods = root.find(xml_tag)

    for _period in _periods:
        if period_type == 'Annual':
            fiscal_period = AnnualFiscalPeriod(**_period.attrib)
        else:
            fiscal_period = InterimFiscalPeriod(**_period.attrib)

        for _statement in _period:
            type = _statement.attrib['Type']
            _iter = iter(_statement)
            _pfheader = next(_iter)
            print(ET.tostring(_pfheader).decode())
            if type != 'BAL':
                period_length = _pfheader.find('PeriodLength').text + _pfheader.find('periodType').attrib['Code']
                print(period_length)
            update_type = {_pfheader.find('UpdateType').attrib['Code']: _pfheader.find('UpdateType').text}
            statement_date = _pfheader.find('StatementDate').text
            source = _pfheader.find('Source').text
            source_date = _pfheader.find('Source').attrib['Date']
            try:
                _auditor_name = _pfheader.find('AuditorName')
                auditor_name = {_auditor_name.attrib['Code']: _auditor_name.text}
                auditor_opinion = {
                    _pfheader.find('AuditorOpinion').attrib['Code']: _pfheader.find('AuditorOpinion').text}
            except:
                print('No Auditor name for annual report')

            statement = {}

            try:
                while True:
                    _item = next(_iter)
                    statement.update({_item.attrib['coaCode']: float(_item.text)})
            except StopIteration:
                pass

            print("statement : {}".format(statement))

            record = Statement()
            record.ticker = ticker
            record.last_modified = last_modified
            record.statement_type = type
            record.fiscal_period = fiscal_period._asdict()
            record.update_type = list(update_type.keys())[0]
            record.statement_date = statement_date
            # record.auditor_name = mongoengine.StringField()
            # record.auditor_opinion = mongoengine.StringField()
            record.source = source
            record.source_date = source_date
            record.statement = statement
            # record = {'Ticker': 'PAYC',
            #           'FiscalPeriod': fiscal_period,
            #           'StatementType': type,
            #           'Statement': statement
            #           }
            #
            # db.FinancialStatements.insert_one(record)

            # check if record in database, if not save to the database
            # if not Statement.objects(ticker=record.ticker,
            #                          period_type=record.fiscal_period,
            #                          statement_type=record.statement_date,
            #                          statement_date=record.statement_date):
            record.save()
