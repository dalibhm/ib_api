from statement_parser import *

from collections import namedtuple
# import mongo_client
# from mongo_client import db

import mongo_setup
mongo_setup.global_init()

Issue = namedtuple('Issue', ['id', 'type', 'desc', 'order', 'issue_ids', 'exchange'])
GeneralInfo = namedtuple('GeneralInfo', ['status', 'type', 'last_modified',
                                         'last_available_annual', 'last_available_interim',
                                         'reporting_currency', 'most_recent_exchange'])

file_name = 'Files/FinancialStatements.xml'
with open(file_name, 'rt') as f:
    data = f.read()

doc = ET.parse(file_name)
root = doc.getroot()

# or from a directly from s string
# root = ET.fromstring(xml_string)


co_ids = {}
for co_id in root.find('CoIDs'):
    # print(ET.tostring(co_id).decode())
    co_ids[co_id.attrib['Type']] = co_id.text

print("coids :{}".format(co_ids))

issues = []
for _issue in root.find('Issues'):
    # print(ET.tostring(_issue).decode())
    issue = Issue(id=_issue.attrib['ID'],
                  type=_issue.attrib['Type'],
                  desc=_issue.attrib['Desc'],
                  order=_issue.attrib['Order'],
                  issue_ids={},
                  exchange={}
                  )
    # for _issue_id in _issue:
    #     print(ET.tostring(_issue_id).decode())
    #     if _issue_id.tag == 'IssueID':
    #         issue.issue_ids.update({_issue_id.attrib['Type']: _issue_id.text})
    issue.issue_ids.update(
        {_issue_id.attrib['Type']: _issue_id.text for _issue_id in _issue if _issue_id.tag == 'IssueID'}
    )
    _exchange = _issue.find('Exchange')
    issue.exchange.update(
        {_exchange.attrib['Code']: (_exchange.text, _exchange.attrib['Country'])}
    )
    issues.append(issue)

print("issues :{}".format(issues))

info: ET.Element
info = root.find('CoGeneralInfo')
# print(ET.tostring(info).decode())
_status = info.find('CoStatus')
_type = info.find('CoType')
_reporting_currency = info.find('ReportingCurrency')
_most_recent_Exchange = info.find('MostRecentExchange')

general_info = GeneralInfo(
    status=(_status.text, _status.attrib['Code']),
    type=(_type.text, _type.attrib['Code']),
    last_modified=info.find('LastModified').text,
    last_available_annual=info.find('LatestAvailableAnnual').text,
    last_available_interim=info.find('LatestAvailableInterim').text,
    reporting_currency=(_reporting_currency.text, _reporting_currency.attrib['Code']),
    most_recent_exchange=(_most_recent_Exchange.text, _most_recent_Exchange.attrib['Date'])
)

print("general_info :{}".format(general_info))

map_items = {}
for map_item in root.find('FinancialStatements/COAMap'):
    attributes = map_item.attrib
    code = attributes.pop('coaItem')
    map_items[code] = attributes
    map_items[code].update({'description': map_item.text})

print("map_items :{}".format(map_items))

save_statements(period_type='Interim',
                root=root,
                ticker=issues[0].issue_ids['Ticker'],
                last_modified=general_info.last_modified)
