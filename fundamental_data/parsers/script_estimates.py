from fundamental_client import Client
import xml.etree.ElementTree as ET
from pprint import pprint

url = '127.0.0.1:12399'
client = Client(server_url=url)

report = client.get_latest_report('PAYC', 'RESC')
xml: ET.Element = ET.fromstring(report.content)

# <Element 'Company' at 0x10cfefb90>
# <Element 'Actuals' at 0x10d01f230>
# <Element 'ConsEstimates' at 0x10d60a230>

for c in list(xml):
    c: ET.Element
    print(c)

    if c.tag == 'Actuals':
        for ccc in list(c):
            for cc in list(ccc):
                cc: ET.Element
                print(cc)
                print('tag', cc.tag)
                print('attributes', cc.attrib)
                print('text', cc.text)
                print('tail', cc.tail)
    else:
        continue
