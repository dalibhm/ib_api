import gzip
import os
import time
from datetime import datetime
from pathlib import Path

# import sys
# sys.path.insert(0, '..')

from mongo_data.mongo_init import global_init
from mongo_data.statement import Statement


def read_content(filename):
    extension = filename.split('.')[-1]
    try:
        if extension == 'xml':
            return read_file_from_xml(filename)
        elif extension == 'gzip':
            return read_file_from_gzip(filename)
    except Exception as e:
        print('ERROR for', filename)
        print(e)


def read_file_from_gzip(file):
    with gzip.open(file, 'rb') as f:
        _content = f.read()
    return _content.decode('ascii')


def read_file_from_xml(file):
    with open(file, 'r') as f:
        _content = f.read()
    return _content

# get unique symbols
def get_symbol_from_filename(_filename, _report_type):
    return _filename.split(_report_type)[0].split('.')[0].split('_')[0]

def symbol_in_filename(_symbol, _filename, _report_type):
    symbol_from_file = get_symbol_from_filename(_filename, _report_type)
    return _symbol == symbol_from_file


'ONE.ReportsFinStatements_0.xml'
'KE_ReportsFinStatements_2019-10-31 02:57:30.612850.xml'
'DEA.DataType.ReportsFinStatements_0.xml'

directories = ['/Users/dali/Documents/Fundamental Data',
               '/Users/dali/workspace/rabbitmq/FundamentalData',
               '/Users/dali/workspace/fundamental_data',
               '/Users/dali/workspace/ib_python/fundamental_data/data',
               '/Users/dali/workspace/ib_python/data_api/tests/financial_data']

report_types = ['ReportsFinStatements',
                'ReportsFinSummary',
                'CalendarReport',
                'RESC',
                'ReportSnapshot',
                'ReportsOwnership']

# database init
global_init()
report_type = report_types[5]

for report_type in report_types:



    files = {}
    # get files from all directories
    for directory in directories:
        rootdir = Path(directory)
        full_path_names = [f.as_posix() for f in rootdir.resolve().glob('**/*{}*'.format(report_type)) if f.is_file()]
        # file_names = glob.glob("*{}*".format(report_type), recursive=True)
        # full_path_names = [os.path.join(directory, filename) for filename in file_names]
        # {file: time.ctime(os.path.getctime(file)) for file in files}
        local_files = {file: os.stat(file).st_birthtime for file in full_path_names}
        files.update(local_files)



    symbols = set([get_symbol_from_filename(os.path.basename(file), report_type) for file in files])

    for symbol in symbols:
        symbol_files = {key: files[key] for key in files.keys() if
                        symbol_in_filename(symbol, os.path.basename(key), report_type)}
        sorted_files = sorted(zip(symbol_files.values(), symbol_files.keys()))
        for creation_date, file_name in sorted_files:
            # if datetime.fromtimestamp(creation_date) < datetime(2019, 11, 3):
            #     continue
            print('-----------------------------------------------------------------------')
            print(file_name, time.ctime(creation_date))
            content = read_content(file_name)
            try:
                content = content.replace('\r', '')
                # print(symbol, content[0:100])
                existing_records = Statement.objects(ticker=symbol, report_type=report_type)
                if existing_records:
                    latest_record = existing_records.first()
                    if content == latest_record.report:
                        continue
                mongo_record = Statement(ticker=symbol,
                                         insert_date=datetime.fromtimestamp(creation_date),
                                         report_type=report_type,
                                         report=content)
                mongo_record.save()
            # except AttributeError:
            #     mongo_record = mongo_data.Statement(ticker=symbol,
            #                                         insert_date=datetime.fromtimestamp(creation_date),
            #                                         report_type=report_type,
            #                                         report=content)
            #     mongo_record.save()
            except Exception as e:
                print(e)
                # raise e

# In Python3 since unpacking is not allowed [1] we can use


# from pathlib import Path
#
# rootdir = Path('/Users/dali/Documents/Fundamental Data')
# # Return a list of regular files only, not directories
# file_list = [f for f in rootdir.glob('**/*') if f.is_file()]
#
# # For absolute paths instead of relative the current dir
# file_list = [f for f in rootdir.resolve().glob('**/*') if f.is_file()]
