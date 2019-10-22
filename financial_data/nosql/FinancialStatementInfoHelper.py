from mongo_documents.FinancialReport.statement import Statement
from mongo_documents.FinancialReport.financial_statement_info import *
import xml.etree.ElementTree as ET


def get_company_ids(root):
    company_ids = {}
    for co_id in root.find('CoIDs'):
        # print(ET.tostring(co_id).decode())
        company_ids[co_id.attrib['Type']] = co_id.text
    return company_ids


def get_issues(root):
    issues = []
    for _issue in root.find('Issues'):
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


def get_general_info(root):
    info: ET.Element
    info = root.find('CoGeneralInfo')
    # print(ET.tostring(info).decode())
    company_status_tag = info.find('CoStatus')
    company_type_tag = info.find('CoType')
    reporting_currency_tag = info.find('ReportingCurrency')
    most_recent_exchange_tag = info.find('MostRecentExchange')
    general_info = GeneralInfo(
        company_status=CodedField(code=company_status_tag.attrib['Code'], value=company_status_tag.text),
        company_type=CodedField(code=company_type_tag.attrib['Code'], value=company_type_tag.text),
        last_modified=info.find('LastModified').text,
        latest_available_annual=info.find('LatestAvailableAnnual').text,
        latest_available_interim=info.find('LatestAvailableInterim').text,
        reporting_currency=CodedField(code=reporting_currency_tag.attrib['Code'],
                                      value=reporting_currency_tag.text),
        most_recent_exchange=DatedIntField(date=most_recent_exchange_tag.attrib['Date'],
                                           value=int(float(most_recent_exchange_tag.text)))
    )

    return general_info
