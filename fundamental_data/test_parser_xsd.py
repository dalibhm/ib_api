import os
import sys
import glob

import xmlschema
from pprint import pprint
from xml.etree import ElementTree

if __name__ == '__main__':
    file = os.path.join('.', 'data', 'MSCI_CalendarReport_2019-10-31 03.33.23.086964.xml')
    # with open(file, 'rt') as f:
    #     data = f.read()

    xs = xmlschema.XMLSchema('cr_100.xsd')
    xt = ElementTree.parse(file)
    root = xt.getroot()
    calendar = xs.elements['WSHData'].decode(root)

    pprint(calendar)
    print('size of calendar dict : {}'.format(sys.getsizeof(calendar)))

    # ReportsFinStatements
    pattern = os.path.join('.', 'data', 'MSCI_ReportsFinStatements*.xml')
    files = glob.glob(pattern)
    file = files[0]
    # with open(file, 'rt') as f:
    #     data = f.read()

    xs = xmlschema.XMLSchema('ReportsFinancialStatements.xsd')
    xt = ElementTree.parse(file)
    root = xt.getroot()
    fin_reports = xs.elements['ReportFinancialStatements'].decode(root)

    pprint(fin_reports)
    print('size of fin_reports dict : {}'.format(sys.getsizeof(fin_reports)))

    # pp.pprint(company_ids)
    # pp.pprint(issues)
    # pp.pprint(general_info)
    # pp.pprint(statement_info)
    # pp.pprint(notes)
    # pp.pprint(annual)
    # pp.pprint(interim)
    #
    # print('size of company_ids dict : {}'.format(sys.getsizeof(company_ids)))
    # print('size of issues dict : {}'.format(sys.getsizeof(issues)))
    # print('size of general_info dict : {}'.format(sys.getsizeof(general_info)))
    # print('size of statement_info dict : {}'.format(sys.getsizeof(statement_info)))
    # print('size of notes dict : {}'.format(sys.getsizeof(notes)))
    # print('size of annual dict : {}'.format(sys.getsizeof(annual)))
    # print('size of interim dict : {}'.format(sys.getsizeof(interim)))



