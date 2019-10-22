from mongo_documents.FinancialReport.statement import Statement
from mongo_documents.FinancialReport.financial_statement_info import *
import xml.etree.ElementTree as ET
from datetime import datetime

from mongo_documents.calendar_report import Earnings, EarningsCallTranscript, ShareHolderMeeting, CalendarReport
from nosql.db_access import


def get_earnings(node: ET.Element):
    items = []
    for earning in node:
        item = {}
        for child_node in earning:
            key = child_node.tag.lower()
            if key in ['period', 'time', 'etype']:
                item[key] = child_node.text
                continue
            if key == 'date':
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y')
                continue
            else:
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y %I:%M:%S%p')
                continue

        items.append(Earnings(**item))
    return items


def get_earning_call_transcripts(node: ET.Element):
    items = []
    for earning_call_transcript in node:
        item = {}
        for child_node in earning_call_transcript:
            key = child_node.tag.lower()
            if key in ['period', 'url']:
                item[key] = child_node.text
                continue
            if key == 'timestamp':
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y %I:%M:%S%p')
                continue

        items.append(EarningsCallTranscript(**item))
    return items


def get_shareholder_meetings(node: ET.Element):
    items = []
    for shareholder_meeting in node:
        item = {}
        for child_node in shareholder_meeting:
            key = child_node.tag.lower()
            if key == 'type':
                item[key] = child_node.text
                continue
            if key == 'date':
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y')
                continue
            else:
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y %I:%M:%S%p')
                continue

        items.append(ShareHolderMeeting(**item))
    return items


class FinancialSummaryParser:
    def __init__(self, xml_file, ticker):
        doc = ET.parse(xml_file)
        self.root = doc.getroot()
        self.ticker = ticker

    def process_calendar_report(self):
        fields = {}
        fields['conids'] = []
        for child in self._root.find('Company'):
            if child.tag == 'Name':
                fields['name'] = child.text
                continue
            if child.tag == 'Ticker':
                fields['ticker'] = child.text
                continue
            if child.tag == 'Exchange':
                fields['Exchange'] = child.text
                continue
            if child.tag == 'Country':
                fields['country'] = child.text
                continue
            if child.tag == 'conid':
                fields['conids'].append(child.text)
                continue
            if child.tag == 'EarningsList':
                fields['earnings'] = get_earnings(child)
                continue
            if child.tag == 'EarningsCallTranscriptList':
                fields['earning_calls_transcripts'] = get_earning_call_transcripts(child)
                continue
            if child.tag == 'ShareHolderMeetingList':
                fields['shareholder_meetings'] = get_shareholder_meetings(child)
                continue
        calendar_report = CalendarReport(**fields)

