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


file_name = 'Files/STK CCK USD SMART_RESC.xml'

doc = ET.parse(file_name)
root = doc.getroot()




for el in root.getchildren():
    print(el)

for fyactual in root.find('Actuals/FYActuals'):
    print(fyactual.tag)
    print(fyactual.attrib)
    print(fyactual.text)
    # print(ET.tostring(actual).decode())
    # currency = div.attrib


