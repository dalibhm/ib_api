from calendar_reports.calendar_report import CalendarReport
from calendar_reports.company import Company
from xml_parsers.calendar_parser import parse_calendar_report


class CalendarBuilder:
    """ Loads calendar from file"""
    @classmethod
    def load(cls, filename):
        with open(filename, 'rt') as f:
            data = f.read()
        calendar = parse_calendar_report(data)
        company = Company(calendar['name'], calendar['ticker'])
        # if len(calendar['earnings']) > 1:
        #     print('company : {}'.format(company.ticker))
        #     raise Exception
        try:
            cal = CalendarReport(company, calendar['earnings'])
        except KeyError as e:
            print('company : {}'.format(company.ticker))
            # raise e

        return cal


if __name__ == '__main__':
    import os, glob

    pattern = os.path.join('/Users/dali/workspace/ib_python/fundamental_data', 'data', '*_CalendarReport*.xml')
    files = glob.glob(pattern)
    file = files[0]
    for file in files:
        calendar = CalendarBuilder.load(file)
        print('Need Update : {}, NextEarnings_date {}'.format(calendar.is_up_to_date, calendar.next_earnings_date))