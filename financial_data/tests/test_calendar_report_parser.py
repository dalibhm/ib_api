# from datetime import datetime
# import os
# from unittest import TestCase
#
# from xmlparser.CalendarReportParser import CalendarReportParser
#
#
# class TestCalendarReportParser(TestCase):
#     def setUp(self):
#         directory = os.path.join('..', 'xmlsample')
#         file = 'SHOP.CalendarReport_0.xml'
#         xml_path = os.path.join(directory, file)
#         with open(xml_path, 'r') as file_reader:
#             self.xml = file_reader.read()
#
#     def test_calendar_report_parser(self):
#         calendar_report = CalendarReportParser(self.xml, 'SHOP')
#         parse()
#         self.assertEqual('q2', calendar_report.period)
#         self.assertEqual(calendar_report.previous_period_date, datetime.strptime('4/30/2019', '%m/%d/%Y'))
#         self.assertEqual(calendar_report.period_date, datetime.strptime('7/30/2019', '%m/%d/%Y'))
