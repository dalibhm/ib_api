from datetime import datetime
from unittest import TestCase

from models.earningscalendar import EarningsCalendar


class TestCalendarReport(TestCase):

    def setUp(self) -> None:
        self.run_date = '7/01/2019'
        self.earnings_calendar_uptodate = EarningsCalendar('1/31/2019', '4/30/2019', '7/31/2019', '11/302019',
                                                           'q3', 'before marker', 'unconfirmed',
                                                           datetime.strptime('7/31/2019', '%m/%d/%Y'),
                                                           '5/29/2019 11:15:04')
        self.earnings_calendar_old = EarningsCalendar('1/31/2019', '4/30/2019', '7/31/2019', '11/30/2019',
                                                      'q2', 'before marker', 'unconfirmed',
                                                      datetime.strptime('4/30/2019', '%m/%d/%Y'),
                                                      '5/29/2019 11:15:04')

    def test_class(self):
        print(self.earnings_calendar_old)
        self.assertFalse(self.earnings_calendar_old.is_up_to_date)
        self.assertTrue(self.earnings_calendar_uptodate)
