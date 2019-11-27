import xml.etree.ElementTree as ET
import glob
import os


from collections import namedtuple

Id = namedtuple('Id', ['asofDate', 'reportType', 'period'])


def get_field(_root, field):
    switcher = {'DividendPerShares': 0, 'TotalRevenues': 1, 'EPSs': 2}

    currency = _root.getchildren()[switcher[field]].attrib['currency']
    for record in _root.find(field):
        # print(ET.tostring(co_id).decode())
        # currency = div.attrib
        print(record.attrib)
        print(record.text)


if __name__ == '__main__':
    pattern = os.path.join('.', 'data', 'MSCI_ReportsFinSummary*.xml')
    files = glob.glob(pattern)
    file = files[0]
    with open(file, 'rt') as f:
        data = f.read()
    # doc = ET.parse(file)
    # root = doc.getroot()

    # or from a directly from s string
    root = ET.fromstring(data)

    get_field(root, 'DividendPerShares')
    get_field(root, 'TotalRevenues')
    get_field(root, 'EPSs')
