from datetime import datetime

from historical_data.historical_data_client import HistoricalDataService


def adjust_request_dates(start_date, end_date, start_db, end_db):
    end_request = None
    start_request = None

    if end_date > end_db:
        if start_date > start_db:
            end_request = end_date
            start_request = end_db
        elif start_date < start_db:
            raise Exception('the request timespan is larger than the database on both sides')
    elif start_date < start_db:
        end_request = start_db
        start_request = start_date
    return start_request, end_request


if __name__ == '__main__':
    url = '127.0.0.1:12599'
    service = HistoricalDataService(url)

    start_date = '2019-10-05'
    end_date = '2020-10-30'
    symbol = 'AAC'

    print('start date', start_date)
    print('end date', end_date)

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    start_db = datetime.strptime(service.get_start_db(symbol), '%Y%m%d')
    end_db = datetime.strptime(service.get_end_db(symbol), '%Y%m%d')

    start_request, end_request = get_request_dates(start_date, end_date, start_db, end_db)

    print('start_request', start_request)
    print('end_request', end_request)
