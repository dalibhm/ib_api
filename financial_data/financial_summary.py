# import xml.etree.ElementTree as ET
from statement_parser import *

from collections import namedtuple
# import mongo_client
# from mongo_client import db

import mongo_setup

mongo_setup.global_init()

Id = namedtuple('Id', ['asofDate', 'reportType', 'period'])


file_name = 'Files/STK CCK USD SMART_ReportsFinSummary.xml'
# with open(file_name, 'rt') as f:
#     data = f.read()

doc = ET.parse(file_name)
root = doc.getroot()


# or from a directly from s string
# root = ET.fromstring(xml_string)

def get_field(_root, field):
    switcher = {'DividendPerShares': 0, 'TotalRevenues': 1, 'EPSs': 2}

    currency = _root.getchildren()[switcher[field]].attrib['currency']
    for record in _root.find(field):
        # print(ET.tostring(co_id).decode())
        # currency = div.attrib
        print(record.attrib)
        print(record.text)


get_field(root, 'DividendPerShares')
get_field(root, 'TotalRevenues')
get_field(root, 'EPSs')