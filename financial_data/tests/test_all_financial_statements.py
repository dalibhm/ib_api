from datetime import datetime
import os

from mongo_documents.FinancialReport.financial_statement_info import FinancialStatementInfo
from mongo_documents.FinancialReport.statement import Statement
from nosql.FinancialStatementParser import FinancialStatementParser
from mongo_setup import global_init

global_init()

directory = '/Users/dali/workspace/rabbitmq/FundamentalData'
files = os.listdir(directory)

print('Processing {} files.'.format(len(files)))

for file in files:
    if 'ReportsFinStatements' in file:
        # file_name = '../Files/FinancialStatements.xml'
        err = False
        file_full_path = os.path.join(directory, file)
        parser = FinancialStatementParser(file_full_path)
        try:
            statement_info = parser.process_financial_statement_info()
            statements = parser.process_financial_statements()
        except:
            print('ERROR on {}'.format(file))
            err = True
        if not err:
            ticker = statement_info.ticker
            look_for_ticker = FinancialStatementInfo.objects().filter(ticker=ticker)
            if not look_for_ticker:
                statement_info.save()
            print('{} -- Stock : {} started.'.format(datetime.now(), ticker))
            # docs = FinancialStatement.objects().filter()
            # docs_projected = list(FinancialStatement.objects().filter().only('general_info__latest_available_annual'))
            #
            # if docs:
            #     for doc in docs:
            #         print('{} issues - ticker : {}'.format(len(doc.issues), doc.issues[0].issue_ids['Ticker']))

            for key in statements.keys():
                for ft in statements[key]:
                    look_for_record = Statement.objects().filter(ticker=ticker,
                                                                 fiscal_period__end_date=ft.fiscal_period.end_date,
                                                                 fiscal_period__type__=ft.fiscal_period.type,
                                                                 type=ft.type).limit(1)
                    if not look_for_record:
                        ft.save()

# datetime.strptime(ft.fiscal_period.end_date, "%Y-%m-%d").date()
# datetime.datetime(2017, 11, 8).date()

