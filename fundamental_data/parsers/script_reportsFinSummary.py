from fundamental_client import Client
import xml.etree.ElementTree as ET
from pprint import pprint

url = '127.0.0.1:12399'
client = Client(server_url=url)

report = client.get_latest_report('PAYC', 'ReportsFinSummary')
xml: ET.Element = ET.fromstring(report.content)

# <Element 'CoIDs' at 0x10ca35b90>
# <Element 'Issues' at 0x10ca35dd0>
# <Element 'CoGeneralInfo' at 0x10ca551d0>
# <Element 'StatementInfo' at 0x10ca554d0>
# <Element 'Notes' at 0x10ca55650>
# <Element 'FinancialStatements' at 0x10ca55890>

for c in list(xml):
    c: ET.Element
    print(c)
    print('tag', c.tag)
    print('attributes', c.attrib)
    print('text', c.text)
    print('tail', c.tail)
    if c.tag == 'EPSs':
        # for ccc in list(c):
        for cc in list(c):
            cc: ET.Element
            print(cc)
            print('tag', cc.tag)
            print('attributes', cc.attrib)
            print('text', cc.text)
            print('tail', cc.tail)
    else:
        continue
