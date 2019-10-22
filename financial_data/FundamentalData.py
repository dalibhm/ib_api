import mongo_setup
from mongo_documents.FinancialReport.statement import Statement

from codes.statement_codes import fields_map

import pandas as pd
mongo_setup.global_init()

# for st: Statement in Statement.objects:
#     print(st.ticker)

# records : Statement = Statement.objects(ticker='PAYC',
#                                      period_type='Interim',
#                                      statement_type='BAL',
#                                      statement_date='2018-06-30')

records : Statement = Statement.objects(ticker='PAYC')
# [print("{} {} {}".format(p.statement_type, p.period_type, p.statement_date)) for p in payc]

df = pd.DataFrame(list(records))


for record in records:
    df = pd.DataFrame(record.statement.items(), columns=['item', 'value'])
    df['statemt_type'] = [fields_map[df['item'][i]].statementType for i in range(0, df.shape[0])]
    df['name'] = [fields_map[df['item'][i]].name for i in range(0, df.shape[0])]
    df['precision'] = [fields_map[df['item'][i]].precision for i in range(0, df.shape[0])]
    df['ticker'] = record.ticker
    df['statement_date'] = record.statement_date
    df['end_fiscal_period'] = record.fiscal_period['EndDate']
    # df['period_type'] = record.period_type
    print('{} {} {} {}'.format(record.statement_type, record.statement_date, record.fiscal_period['Type'], record.fiscal_period['EndDate']))
    # total[total['item'] == 'AACR']
    try:
        total = pd.concat([total, df]).reset_index(drop=True)
    except NameError:
        total = pd.DataFrame(data=None, columns=df.columns)

total.pivot(index='item', columns='end_fiscal_period').to_csv('pivot.csv')
    # pd.Series(record.statement, index=record.statement.keys())

# with open('file.csv', 'w') as f:
#     for record in records:
#         # print(type(record.statement))
#         for key in record.statement:
#             print(fields_map[key].name, end=';', file=f)
#             print(key, end=';', file=f)
#             print(fields_map[key].statementType, end=';', file=f)
#             print(fields_map[key].lineID, end=';', file=f)
#             print(fields_map[key].precision, end=';', file=f)
#             print(record.statement[key], end=';', file=f)
#             print(record.statement_type, end=';', file=f)
#             print(record.ticker, end=';', file=f)
#             print(record.last_modified, end=';', file=f)
#             print(record.period_type, end=';', file=f)
#             print(record.update_type, end=';', file=f)
#             print(record.statement_date, end=';', file=f)
#             print(record.source, end=';', file=f)
#             print(record.source_date, end=';', file=f)
#             print(record.insert_date, file=f)




