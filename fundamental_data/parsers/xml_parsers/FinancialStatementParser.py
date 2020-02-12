import xml.etree.ElementTree as ET

from .FinancialStatementHelper import process_statements
from .FinancialStatementInfoHelper import get_company_ids, get_issues, get_general_info, parse_statement_info, \
    parse_notes


def parse_financial_statements(xml_string):
    company_ids = None
    issues = None
    general_info = None
    statement_info = None
    notes = None
    root = ET.fromstring(xml_string)
    for node in root:
        tag = node.tag.lower()
        if tag == 'coids':
            company_ids = get_company_ids(node)
            continue
        if tag == 'issues':
            issues = get_issues(node)
            continue
        if tag == 'cogeneralinfo':
            general_info = get_general_info(node)
            continue
        if tag == 'statementinfo':
            statement_info = parse_statement_info(node)
            continue
        if tag == 'notes':
            notes = parse_notes(node)
            continue
        if tag != 'financialstatements':
            # annual, interim = parse_statements(root)
            raise TypeError

    annual, interim = process_statements(root)
    return company_ids, issues, general_info, statement_info, notes, annual, interim
