import datetime

from dateutil.relativedelta import relativedelta

from custom_types.request_type import RequestType


class RequestTemplate:
    def __init__(self):
        pass


import logging

logger = logging.getLogger(__name__)


class HistoricalRequestTemplate(RequestTemplate):
    def __init__(self, param_config):
        self.type = RequestType.Historical
        start_date = datetime.datetime.strptime(param_config['start_date'], '%Y-%m-%d')
        end_date = datetime.datetime.strptime(param_config['end_date'], '%Y-%m-%d')
        bar_size = param_config['bar_size']
        price_type = param_config['price_type']

        period_length = relativedelta(end_date, start_date)
        if period_length.days < 0 or period_length.months < 0 or period_length.years < 0 :
            logging.error('the start date in the database is more recent than the end date')
            raise Exception('the start date in the database is more recent than the end date')

        if period_length.years > 0:
            period_length = period_length.years
            period_unit = 'Y'
        elif period_length.months > 0:
            period_length = period_length.months
            period_unit = 'M'
        else:
            period_length = period_length.days
            period_unit = 'D'
        historical_data_length = '{} {}'.format(period_length, period_unit)

        self.params = {'endDateTime': end_date.strftime("%Y%m%d %H:%M:%S"),
                       'durationString': historical_data_length,
                       'barSizeSetting': bar_size,
                       'whatToShow': price_type,  # price_type.name
                       'useRTH': 1,
                       'formatDate': 1,
                       'keepUpToDate': 0
                       }


class FundamentalRequestTemplate(RequestTemplate):
    def __init__(self, param_config):
        self.type = RequestType.Fundamental
        self.params = param_config['report_types']
