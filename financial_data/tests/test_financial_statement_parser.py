import os
from unittest import TestCase

from xmlparser.FinancialStatementParser import FinancialStatementParser, parse_financial_statements


class TestFinancialStatementParser(TestCase):

    def setUp(self):
        self.directory = '/Users/dali/Documents/Fundamental Data/20190706/NYSE/_financial_reports'
        with open('/Users/dali/Documents/Fundamental Data/20190706/NYSE/_stock_list.txt') as f:
            self.stocks = f.read().splitlines()

    def test_read_financial_statements(self):
        financial_statement_file = os.path.join(self.directory, '{}.ReportsFinStatements_0.xml'.format(self.stocks[1000]))
        with open(financial_statement_file) as f:
            xml = f.read()
        annual, interim = parse_financial_statements(xml)
        for statement in annual:
            print(statement)
        for statement in interim:
            print(statement)

    def test_read_financial_parser(self):
        financial_statement_file = os.path.join(self.directory, '{}.ReportsFinStatements_0.xml'.format(self.stocks[1000]))
        with open(financial_statement_file) as f:
            xml = f.read()
        a, b, c, d, e, annual, interim = parse_financial_statements(xml)
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        # for statement in annual:
        #     print(statement)
        # for statement in interim:
        #     print(statement)