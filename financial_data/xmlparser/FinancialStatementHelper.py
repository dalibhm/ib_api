import xml.etree.ElementTree as ET
from collections import namedtuple

from mongo_documents.FinancialReport.CommonFields import CodedField
from mongo_documents.FinancialReport.statement import FiscalPeriod, StatementInfo, Statement
from nosql.db_access import write_financial_statement

AnnualFiscalPeriod = namedtuple('AnnualFiscalPeriod', ['Type', 'EndDate', 'FiscalYear'])
InterimFiscalPeriod = namedtuple('InterimFiscalPeriod', ['Type', 'EndDate', 'FiscalYear', 'FiscalPeriodNumber'])


def get_fiscal_period(_period):
    period_type = _period.attrib['Type']
    if period_type == 'Annual':
        fiscal_period = FiscalPeriod(
            type=_period.attrib['Type'],
            end_date=_period.attrib['EndDate'],
            fiscal_year=_period.attrib['FiscalYear']
        )
    else:
        fiscal_period = FiscalPeriod(
            type=_period.attrib['Type'],
            end_date=_period.attrib['EndDate'],
            fiscal_year=_period.attrib['FiscalYear'],
            fiscal_period_number=_period.attrib['FiscalPeriodNumber']
        )
    return fiscal_period


def process_statement(_periods):
    statements = []
    for _period in _periods:
        fiscal_period = get_fiscal_period(_period)

        for _statement in _period:
            statement = Statement()
            # statement.ticker = ticker
            statement.fiscal_period = fiscal_period
            statement_type = _statement.attrib['Type']
            statement.type = statement_type
            # print('statement_type : {}'.format(statement_type))
            _iter = iter(_statement)
            _pfheader = next(_iter)
            statement_info = StatementInfo()
            # print(ET.tostring(_pfheader).decode())
            if statement_type != 'BAL':
                statement_info.period_length = _pfheader.find('PeriodLength').text
                _period_type = _pfheader.find('periodType')
                if _period_type:
                    statement_info.period_type = CodedField(_period_type.attrib['Code'],
                                                            _period_type.text)
                # print(period_length)
            statement_info.update_type = CodedField(_pfheader.find('UpdateType').attrib['Code'],
                                                    _pfheader.find('UpdateType').text)
            statement_info.statement_date = _pfheader.find('StatementDate').text
            statement_info.source = _pfheader.find('Source').text
            statement_info.source_date = _pfheader.find('Source').attrib['Date']
            try:
                _auditor_name = _pfheader.find('AuditorName')
                statement_info.auditor_name = CodedField(_auditor_name.attrib['Code'],
                                                         _auditor_name.text)
                statement_info.auditor_opinion = CodedField(_pfheader.find('AuditorOpinion').attrib['Code'],
                                                            _pfheader.find('AuditorOpinion').text)
            except:
                pass
            #     print('No Auditor name for annual report')

            statement.statement_info = statement_info

            statement_dic = {}
            try:
                while True:
                    _item = next(_iter)
                    statement_dic.update({_item.attrib['coaCode']: float(_item.text)})
            except StopIteration:
                pass

            statement.statement = statement_dic
            statements.append(statement)
    return statements


def process_statements(root):
    period_types = ['Annual', 'Interim']
    statements = {}
    for period_type in period_types:
        xml_tag = 'FinancialStatements/{}Periods'.format(period_type)
        _periods = root.find(xml_tag)
        period_statements = process_statement(_periods)
        statements[period_type] = period_statements
    return statements['Annual'], statements['Interim']
