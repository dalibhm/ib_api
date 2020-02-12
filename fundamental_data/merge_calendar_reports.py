import glob
import os
import sys
from xml.etree import ElementTree

if __name__ == '__main__':
    pattern = os.path.join('.', 'data', '*_CalendarReport*.xml')
    files = glob.glob(pattern)

    # output = ElementTree.Element('data')
    top = ElementTree.Element('data')
    for file in files:
        xt = ElementTree.parse(file)
        root = xt.getroot()
        top.append(root)

    # outpututput.write('cr_100.xml')
    ElementTree.ElementTree(top).write('cr_100.xml')
