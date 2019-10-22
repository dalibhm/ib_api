from nosql.FinancialStatementParser import FinancialStatementParser
from mongo_setup import global_init

global_init()

file_name = '../Files/FinancialStatements.xml'
file_name = '/Users/dali/workspace/rabbitmq/FundamentalData/BFST.DataType.ReportsFinStatements_0.xml'
parser = FinancialStatementParser(file_name)
statements = parser.process_financial_statements()
statement_info = parser.process_financial_statement_info()

statement_info.save()
ticker = statement_info.issues[0].issue_ids['Ticker']
# docs = FinancialStatement.objects().filter()
# docs_projected = list(FinancialStatement.objects().filter().only('general_info__latest_available_annual'))
#
# if docs:
#     for doc in docs:
#         print('{} issues - ticker : {}'.format(len(doc.issues), doc.issues[0].issue_ids['Ticker']))

for key in statements.keys():
    for ft in statements[key]:
        ft.ticker = ticker
        ft.save()
