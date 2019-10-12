import os
import shutil
from os.path import isfile, join, exists

import scripts.__init__
from sql_data.Contract import Contract
from sql_data.db_factory import DbSessionFactory

calendar_reports_directory = '/Users/dali/Documents/Fundamental Data/20190706/NYSE'
exchange = 'NYSE'

files = [f for f in os.listdir(calendar_reports_directory)
         if isfile(join(calendar_reports_directory, f))
         and f.endswith('.xml')
         and 'CalendarReport' in f]

print(len(files))
calendar_stocks = [f.split('.')[0] for f in files]

session = DbSessionFactory.create_session()
results = session.query(Contract).filter(Contract.primaryExchange == "NYSE")
session.close()

db_stocks = [r.symbol for r in results]
exchange_stocks = set(db_stocks).intersection(calendar_stocks)

# exchange_directory = join(calendar_reports_directory, exchange)
# if not exists(exchange_directory):
#     os.makedirs(exchange_directory)

stock_list_file = join(calendar_reports_directory, '_stock_list.txt')
with open(stock_list_file, 'w') as file:
    for stock in sorted(exchange_stocks):
        file.write('{}\n'.format(stock))

# for stock in exchange_stocks:
#     file_name = '{}.CalendarReport_0.xml'.format(stock)
#     _from = join(calendar_reports_directory, file_name)
#     _to = join(exchange_directory, file_name)
#     shutil.move(_from, _to)
