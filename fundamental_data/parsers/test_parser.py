import os
import pprint as pp
import sys
import glob

from pytest import fixture
import xml.etree.ElementTree as ET

from fundamental_client import Client
from xml_parsers.calendar_parser import parse_calendar_report

from xml_parsers.FinancialStatementParser import parse_financial_statements

if __name__ == '__main__':
    url = '127.0.0.1:12399'
    client = Client(server_url=url)

    file = os.path.join('.', 'data', 'MSCI_CalendarReport_2019-10-31 03.33.23.086964.xml')
    with open(file, 'rt') as f:
        data = f.read()

    calendar = parse_calendar_report(data)
    pp.pprint(calendar)
    print('size of calendar dict : {}'.format(sys.getsizeof(calendar)))

    # ReportsFinStatements
    pattern = os.path.join('.', 'data', 'MSCI_ReportsFinStatements*.xml')
    files = glob.glob(pattern)
    file = files[0]
    with open(file, 'rt') as f:
        data = f.read()

    company_ids, issues, general_info, statement_info, notes, annual, interim = parse_financial_statements(data)
    pp.pprint(company_ids)
    pp.pprint(issues)
    pp.pprint(general_info)
    pp.pprint(statement_info)
    pp.pprint(notes)
    pp.pprint(annual)
    pp.pprint(interim)

    print('size of company_ids dict : {}'.format(sys.getsizeof(company_ids)))
    print('size of issues dict : {}'.format(sys.getsizeof(issues)))
    print('size of general_info dict : {}'.format(sys.getsizeof(general_info)))
    print('size of statement_info dict : {}'.format(sys.getsizeof(statement_info)))
    print('size of notes dict : {}'.format(sys.getsizeof(notes)))
    print('size of annual dict : {}'.format(sys.getsizeof(annual)))
    print('size of interim dict : {}'.format(sys.getsizeof(interim)))



