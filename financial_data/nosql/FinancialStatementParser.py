from mongo_documents.FinancialReport.financial_statement_info import *
import xml.etree.ElementTree as ET

from xmlparser.FinancialStatementHelper import process_statements
from nosql.FinancialStatementInfoHelper import get_company_ids, get_issues, get_general_info
from nosql.db_access import write_financial_statement_info


class FinancialStatementParser:
    def __init__(self, xml_file):
        doc = ET.parse(xml_file)
        self.root = doc.getroot()
        self.ticker = ''

    def process_financial_statement_info(self):
        issues = get_issues(self.root)
        self.ticker = issues[0].issue_ids['Ticker']
        fs_info = FinancialStatementInfo(
            ticker=self.ticker,
            company_ids=get_company_ids(self.root),
            issues=issues,
            general_info=get_general_info(self.root)
        )
        write_financial_statement_info(fs_info, self.ticker)

    def process_financial_statements(self):
        self.process_financial_statement_info()
        process_statements(self.root, self.ticker)


