from mongo_documents.FinancialReport.statement import Statement
from mongo_documents.FinancialReport.financial_statement_info import *
import xml.etree.ElementTree as ET


def get_company_ids(node):
    company_ids = {}
    for co_id in node:
        # print(ET.tostring(co_id).decode())
        company_ids[co_id.attrib['Type']] = co_id.text
    return company_ids


def get_issues(node):
    issues = []
    for _issue in node:
        # print(ET.tostring(_issue).decode())
        exchange_tag = _issue.find('Exchange')

        issue = Issue(id=_issue.attrib['ID'],
                      type=_issue.attrib['Type'],
                      desc=_issue.attrib['Desc'],
                      order=_issue.attrib['Order'],
                      issue_ids={_issue_id.attrib['Type']: _issue_id.text
                                 for _issue_id in _issue
                                 if _issue_id.tag == 'IssueID'},
                      exchange=Exchange(code=exchange_tag.attrib['Code'],
                                        country=exchange_tag.attrib['Country'],
                                        name=exchange_tag.text)
                      )
        issues.append(issue)
    return issues


def get_general_info(node):
    node: ET.Element
    company_status_tag = node.find('CoStatus')
    company_type_tag = node.find('CoType')
    reporting_currency_tag = node.find('ReportingCurrency')
    most_recent_exchange_tag = node.find('MostRecentExchange')
    general_info = GeneralInfo(
        company_status=CodedField(code=company_status_tag.attrib['Code'], value=company_status_tag.text),
        company_type=CodedField(code=company_type_tag.attrib['Code'], value=company_type_tag.text),
        last_modified=node.find('LastModified').text,
        latest_available_annual=node.find('LatestAvailableAnnual').text,
        latest_available_interim=node.find('LatestAvailableInterim').text,
        reporting_currency=CodedField(code=reporting_currency_tag.attrib['Code'],
                                      value=reporting_currency_tag.text),
        most_recent_exchange=DatedIntField(date=most_recent_exchange_tag.attrib['Date'],
                                           value=int(float(most_recent_exchange_tag.text)))
    )

    return general_info


def parse_statement_info(node: ET.Element):
    result = {}
    child_node: ET.Element
    for child_node in node:
        tag = child_node.tag
        if tag in ['COAType', 'BalanceSheetDisplay', 'CashFlowMethod']:
            result[tag] = {'code': child_node.attrib['Code'], 'value': child_node.text}
        else:
            raise TypeError
    return result


def parse_notes(node: ET.Element):
    result = {}
    child_node: ET.Element
    for child_node in node:
        tag = child_node.tag
        if tag in ['CFAAvailability', 'IAvailability', 'ISIAvailability', 'BSIAvailability', 'CFIAvailability']:
            result[tag] = child_node.attrib['Code']
        else:
            raise TypeError
    return result
