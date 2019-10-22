from nosql.FinancialStatementParser import FinancialStatementParser
from mongo_setup import global_init

from mongo_documents.FinancialReport.financial_statement_info import FinancialStatementInfo

file_name = '../Files/FinancialStatements.xml'
parser = FinancialStatementParser(file_name)
mongo_document = parser.process_financial_statements()
print(mongo_document)

global_init()
docs = FinancialStatementInfo.objects().filter()
docs_projected = list(FinancialStatementInfo.objects().filter().only('general_info__latest_available_annual'))

if docs:
    for doc in docs:
        print('{} issues - ticker : {}'.format(len(doc.issues), doc.issues[0].issue_ids['Ticker']))
mongo_document.save()
