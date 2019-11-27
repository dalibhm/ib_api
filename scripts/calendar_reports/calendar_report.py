import datetime

NB_DAYS = 3


def get_most_recent_earnings(earnings):
    max_index = 0
    for i in range(1, len(earnings)):
        if earnings[i]['timestamp'] > earnings[max_index]['timestamp']:
            max_index = i
    return earnings[max_index]


class CalendarReport:
    def __init__(self, company, earnings):
        self.company = company
        if len(earnings) > 0:
            earnings = get_most_recent_earnings(earnings)
        self.__period = earnings['period']
        self.date = earnings['date'].date()
        self.time = earnings['time']
        self.etype = earnings['etype']
        self.earnings_dates = {k.upper(): earnings[k] for k in ['q1', 'q2', 'q3', 'q4']}
        # verify timestamp = time of writing the file
        self.timestamp = earnings['timestamp']

    @property
    def period(self):
        return self.__period

    @property
    def next_earnings_date(self):
        return self.date

    @property
    def need_update(self):
        return self.next_earnings_date <= datetime.date.today() - NB_DAYS

    def __repr__(self):
        return '{} - next earning date: {} + period : {} + time {} + timestamp {}'.format(self.company.ticker, self.date, self.__period, self.time, self.timestamp)