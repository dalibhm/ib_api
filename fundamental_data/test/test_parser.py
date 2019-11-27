import os

from pytest import fixture
import xml.etree.ElementTree as ET

from xml_parsers.calendar_parser import parse_calendar_report


@fixture
def calendar_xml():
    file = os.path.join('.', 'data', 'MSCI_CalendarReport_2019-10-31 03.33.23.086964.xml')
    with open(file, 'rt') as f:
        data = f.read()
    return data


def test_calendar_parser(calendar_xml):
    calendar = parse_calendar_report(calendar_xml)
    assert 1 == 2
