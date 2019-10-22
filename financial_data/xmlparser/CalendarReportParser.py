import xml.etree.ElementTree as ET
from datetime import datetime


def parse_calendar_report(xml_string):
    root = ET.fromstring(xml_string)
    fields = {'conids': []}
    for child in root.find('Company'):
        tag = child.tag.lower()
        if tag in ['name', 'ticker', 'Exchange', 'Country']:
            fields[tag] = child.text
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
    return fields


# class CalendarReportParser:
#     def __init__(self):
#
#         self.ticker = ticker
#         self.fields = None
#
#     @property
#     def period(self):
#         return self.fields['earnings'][0]['period'].lower()  # why is there an earning list?
#         # test the existence of multiple earnings on a sample
#
#     @property
#     def period_date(self):
#         return self.fields['earnings'][0]['date']
#
#     @property
#     def previous_period_date(self):
#         return self.fields['earnings'][0][previous_period[self.period]]


previous_period = {'q1': 'q4',
                   'q2': 'q1',
                   'q3': 'q2',
                   'q4': 'q3'}


def get_earnings(node: ET.Element):
    items = []
    for earning in node:
        item = {}
        for child_node in earning:
            key = child_node.tag.lower()
            if key in ['period', 'time', 'etype']:
                item[key] = child_node.text
                continue
            if key in ['q1', 'q2', 'q3', 'q4', 'date']:
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y')
                continue
            else:
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y %I:%M:%S %p')
                continue

        items.append(item)
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
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y %I:%M:%S %p')
                continue

        items.append(item)
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
                item[key] = datetime.strptime(child_node.text, '%m/%d/%Y %I:%M:%S %p')
                continue

        items.append(item)
    return items
