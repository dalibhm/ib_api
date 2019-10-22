# import xml.etree.ElementTree as ET
from statement_parser import *

from collections import namedtuple
# import mongo_client
# from mongo_client import db

import mongo_setup

mongo_setup.global_init()

##########################################
#    to be understood and completed
##########################################

Ratio = namedtuple('Ratio', ['FieldName', 'Type', 'PeriodType', 'Value'])


file_name = 'Files/STK CCK USD SMART_ReportSnapshot.xml'

doc = ET.parse(file_name)
root = doc.getroot()




for el in root.getchildren():
    print(el)

for ratio in root.find('ForecastData'):
    # print(ET.tostring(co_id).decode())
    # currency = div.attrib
    fieldName = ratio.attrib['FieldName']
    type = ratio.attrib['Type']
    for value in ratio.getchildren():
        periodType = value.attrib['PeriodType']
        v = value.text
    record = Ratio(
        fieldName, type, periodType, v
    )

    print(record)
    # print(ET.tostring(record))

