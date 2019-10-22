import xml.etree.ElementTree as ET

from mongo_documents.FinancialSummary.financial_summary import FinancialSummary
from nosql.db_access import write_financial_summary


class FinancialSummaryParser:
    def __init__(self, xml_file, ticker):
        doc = ET.parse(xml_file)
        self.root = doc.getroot()
        self.ticker = ticker

    def process_financial_summary(self):
        get_field(self.root, self.ticker, 'DividendPerShare')
        get_field(self.root, self.ticker, 'TotalRevenue')
        get_field(self.root, self.ticker, 'EPS')


def get_field(_root, ticker, field):
    switcher = {'DividendPerShare': 0, 'TotalRevenue': 1, 'EPS': 2}

    currency = _root.getchildren()[switcher[field]].attrib['currency']
    for record in _root.find(field):
        summary_record = FinancialSummary(ticker=ticker,
                                          currency=currency,
                                          data_type=field,
                                          as_of_date=record.attrib['asofDate'],
                                          report_type=record.attrib['reportType'],
                                          period=record.attrib['period'],
                                          value=float(record.text)
                                          )
        write_financial_summary(summary_record)