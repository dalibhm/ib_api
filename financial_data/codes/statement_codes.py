import xml.etree.ElementTree as ET
from collections import namedtuple

xml_string = """
<COAMap>
<mapItem coaItem="SREV" statementType="INC" lineID="100" precision="1">Revenue</mapItem>
<mapItem coaItem="SORE" statementType="INC" lineID="300" precision="1">Other Revenue, Total</mapItem>
<mapItem coaItem="RTLR" statementType="INC" lineID="310" precision="1">Total Revenue</mapItem>
<mapItem coaItem="SCOR" statementType="INC" lineID="360" precision="1">Cost of Revenue, Total</mapItem>
<mapItem coaItem="SGRP" statementType="INC" lineID="370" precision="1">Gross Profit</mapItem>
<mapItem coaItem="SSGA" statementType="INC" lineID="550" precision="1">Selling/General/Admin. Expenses, Total</mapItem>
<mapItem coaItem="ERAD" statementType="INC" lineID="560" precision="1">Research &amp; Development</mapItem>
<mapItem coaItem="SDPR" statementType="INC" lineID="600" precision="1">Depreciation/Amortization</mapItem>
<mapItem coaItem="SINN" statementType="INC" lineID="671" precision="1">Interest Exp.(Inc.),Net-Operating, Total</mapItem>
<mapItem coaItem="SUIE" statementType="INC" lineID="740" precision="1">Unusual Expense (Income)</mapItem>
<mapItem coaItem="SOOE" statementType="INC" lineID="820" precision="1">Other Operating Expenses, Total</mapItem>
<mapItem coaItem="ETOE" statementType="INC" lineID="830" precision="1">Total Operating Expense</mapItem>
<mapItem coaItem="SOPI" statementType="INC" lineID="840" precision="1">Operating Income</mapItem>
<mapItem coaItem="SNIN" statementType="INC" lineID="911" precision="1">Interest Inc.(Exp.),Net-Non-Op., Total</mapItem>
<mapItem coaItem="NGLA" statementType="INC" lineID="920" precision="1">Gain (Loss) on Sale of Assets</mapItem>
<mapItem coaItem="SONT" statementType="INC" lineID="1270" precision="1">Other, Net</mapItem>
<mapItem coaItem="EIBT" statementType="INC" lineID="1280" precision="1">Net Income Before Taxes</mapItem>
<mapItem coaItem="TTAX" statementType="INC" lineID="1290" precision="1">Provision for Income Taxes</mapItem>
<mapItem coaItem="TIAT" statementType="INC" lineID="1300" precision="1">Net Income After Taxes</mapItem>
<mapItem coaItem="CMIN" statementType="INC" lineID="1310" precision="1">Minority Interest</mapItem>
<mapItem coaItem="CEIA" statementType="INC" lineID="1320" precision="1">Equity In Affiliates</mapItem>
<mapItem coaItem="CGAP" statementType="INC" lineID="1330" precision="1">U.S. GAAP Adjustment</mapItem>
<mapItem coaItem="NIBX" statementType="INC" lineID="1340" precision="1">Net Income Before Extra. Items</mapItem>
<mapItem coaItem="STXI" statementType="INC" lineID="1390" precision="1">Total Extraordinary Items</mapItem>
<mapItem coaItem="NINC" statementType="INC" lineID="1400" precision="1">Net Income</mapItem>
<mapItem coaItem="SANI" statementType="INC" lineID="1460" precision="1">Total Adjustments to Net Income</mapItem>
<mapItem coaItem="CIAC" statementType="INC" lineID="1470" precision="1">Income Available to Com Excl ExtraOrd</mapItem>
<mapItem coaItem="XNIC" statementType="INC" lineID="1480" precision="1">Income Available to Com Incl ExtraOrd</mapItem>
<mapItem coaItem="SDAJ" statementType="INC" lineID="1520" precision="1">Dilution Adjustment</mapItem>
<mapItem coaItem="SDNI" statementType="INC" lineID="1530" precision="1">Diluted Net Income</mapItem>
<mapItem coaItem="SDWS" statementType="INC" lineID="1540" precision="2">Diluted Weighted Average Shares</mapItem>
<mapItem coaItem="SDBF" statementType="INC" lineID="1550" precision="3">Diluted EPS Excluding ExtraOrd Items</mapItem>
<mapItem coaItem="DDPS1" statementType="INC" lineID="1570" precision="3">DPS - Common Stock Primary Issue</mapItem>
<mapItem coaItem="VDES" statementType="INC" lineID="1770" precision="3">Diluted Normalized EPS</mapItem>
<mapItem coaItem="ACSH" statementType="BAL" lineID="10" precision="1">Cash</mapItem>
<mapItem coaItem="ACAE" statementType="BAL" lineID="20" precision="1">Cash &amp; Equivalents</mapItem>
<mapItem coaItem="ASTI" statementType="BAL" lineID="30" precision="1">Short Term Investments</mapItem>
<mapItem coaItem="SCSI" statementType="BAL" lineID="40" precision="1">Cash and Short Term Investments</mapItem>
<mapItem coaItem="AACR" statementType="BAL" lineID="70" precision="1">Accounts Receivable - Trade, Net</mapItem>
<mapItem coaItem="ATRC" statementType="BAL" lineID="100" precision="1">Total Receivables, Net</mapItem>
<mapItem coaItem="AITL" statementType="BAL" lineID="180" precision="1">Total Inventory</mapItem>
<mapItem coaItem="APPY" statementType="BAL" lineID="190" precision="1">Prepaid Expenses</mapItem>
<mapItem coaItem="SOCA" statementType="BAL" lineID="260" precision="1">Other Current Assets, Total</mapItem>
<mapItem coaItem="ATCA" statementType="BAL" lineID="270" precision="1">Total Current Assets</mapItem>
<mapItem coaItem="APTC" statementType="BAL" lineID="520" precision="1">Property/Plant/Equipment, Total - Gross</mapItem>
<mapItem coaItem="ADEP" statementType="BAL" lineID="530" precision="1">Accumulated Depreciation, Total</mapItem>
<mapItem coaItem="APPN" statementType="BAL" lineID="540" precision="1">Property/Plant/Equipment, Total - Net</mapItem>
<mapItem coaItem="AGWI" statementType="BAL" lineID="570" precision="1">Goodwill, Net</mapItem>
<mapItem coaItem="AINT" statementType="BAL" lineID="600" precision="1">Intangibles, Net</mapItem>
<mapItem coaItem="SINV" statementType="BAL" lineID="690" precision="1">Long Term Investments</mapItem>
<mapItem coaItem="ALTR" statementType="BAL" lineID="710" precision="1">Note Receivable - Long Term</mapItem>
<mapItem coaItem="SOLA" statementType="BAL" lineID="780" precision="1">Other Long Term Assets, Total</mapItem>
<mapItem coaItem="ATOT" statementType="BAL" lineID="880" precision="1">Total Assets</mapItem>
<mapItem coaItem="LAPB" statementType="BAL" lineID="890" precision="1">Accounts Payable</mapItem>
<mapItem coaItem="LPBA" statementType="BAL" lineID="900" precision="1">Payable/Accrued</mapItem>
<mapItem coaItem="LAEX" statementType="BAL" lineID="910" precision="1">Accrued Expenses</mapItem>
<mapItem coaItem="LSTD" statementType="BAL" lineID="1120" precision="1">Notes Payable/Short Term Debt</mapItem>
<mapItem coaItem="LCLD" statementType="BAL" lineID="1130" precision="1">Current Port. of  LT Debt/Capital Leases</mapItem>
<mapItem coaItem="SOCL" statementType="BAL" lineID="1220" precision="1">Other Current liabilities, Total</mapItem>
<mapItem coaItem="LTCL" statementType="BAL" lineID="1230" precision="1">Total Current Liabilities</mapItem>
<mapItem coaItem="LLTD" statementType="BAL" lineID="1240" precision="1">Long Term Debt</mapItem>
<mapItem coaItem="LCLO" statementType="BAL" lineID="1250" precision="1">Capital Lease Obligations</mapItem>
<mapItem coaItem="LTTD" statementType="BAL" lineID="1260" precision="1">Total Long Term Debt</mapItem>
<mapItem coaItem="STLD" statementType="BAL" lineID="1270" precision="1">Total Debt</mapItem>
<mapItem coaItem="SBDT" statementType="BAL" lineID="1300" precision="1">Deferred Income Tax</mapItem>
<mapItem coaItem="LMIN" statementType="BAL" lineID="1310" precision="1">Minority Interest</mapItem>
<mapItem coaItem="SLTL" statementType="BAL" lineID="1370" precision="1">Other Liabilities, Total</mapItem>
<mapItem coaItem="LTLL" statementType="BAL" lineID="1380" precision="1">Total Liabilities</mapItem>
<mapItem coaItem="SRPR" statementType="BAL" lineID="1410" precision="1">Redeemable Preferred Stock, Total</mapItem>
<mapItem coaItem="SPRS" statementType="BAL" lineID="1460" precision="1">Preferred Stock - Non Redeemable, Net</mapItem>
<mapItem coaItem="SCMS" statementType="BAL" lineID="1490" precision="1">Common Stock, Total</mapItem>
<mapItem coaItem="QPIC" statementType="BAL" lineID="1500" precision="1">Additional Paid-In Capital</mapItem>
<mapItem coaItem="QRED" statementType="BAL" lineID="1510" precision="1">Retained Earnings (Accumulated Deficit)</mapItem>
<mapItem coaItem="QTSC" statementType="BAL" lineID="1520" precision="1">Treasury Stock - Common</mapItem>
<mapItem coaItem="QEDG" statementType="BAL" lineID="1530" precision="1">ESOP Debt Guarantee</mapItem>
<mapItem coaItem="QUGL" statementType="BAL" lineID="1540" precision="1">Unrealized Gain (Loss)</mapItem>
<mapItem coaItem="SOTE" statementType="BAL" lineID="1590" precision="1">Other Equity, Total</mapItem>
<mapItem coaItem="QTLE" statementType="BAL" lineID="1600" precision="1">Total Equity</mapItem>
<mapItem coaItem="QTEL" statementType="BAL" lineID="1610" precision="1">Total Liabilities &amp; Shareholders' Equity</mapItem>
<mapItem coaItem="QTCO" statementType="BAL" lineID="1660" precision="2">Total Common Shares Outstanding</mapItem>
<mapItem coaItem="QTPO" statementType="BAL" lineID="1770" precision="2">Total Preferred Shares Outstanding</mapItem>
<mapItem coaItem="STBP" statementType="BAL" lineID="1980" precision="3">Tangible Book Value per Share, Common Eq</mapItem>
<mapItem coaItem="ONET" statementType="CAS" lineID="10" precision="1">Net Income/Starting Line</mapItem>
<mapItem coaItem="SDED" statementType="CAS" lineID="40" precision="1">Depreciation/Depletion</mapItem>
<mapItem coaItem="SAMT" statementType="CAS" lineID="80" precision="1">Amortization</mapItem>
<mapItem coaItem="OBDT" statementType="CAS" lineID="90" precision="1">Deferred Taxes</mapItem>
<mapItem coaItem="SNCI" statementType="CAS" lineID="170" precision="1">Non-Cash Items</mapItem>
<mapItem coaItem="SOCF" statementType="CAS" lineID="470" precision="1">Changes in Working Capital</mapItem>
<mapItem coaItem="OTLO" statementType="CAS" lineID="480" precision="1">Cash from Operating Activities</mapItem>
<mapItem coaItem="SCEX" statementType="CAS" lineID="520" precision="1">Capital Expenditures</mapItem>
<mapItem coaItem="SICF" statementType="CAS" lineID="670" precision="1">Other Investing Cash Flow Items, Total</mapItem>
<mapItem coaItem="ITLI" statementType="CAS" lineID="680" precision="1">Cash from Investing Activities</mapItem>
<mapItem coaItem="SFCF" statementType="CAS" lineID="730" precision="1">Financing Cash Flow Items</mapItem>
<mapItem coaItem="FCDP" statementType="CAS" lineID="760" precision="1">Total Cash Dividends Paid</mapItem>
<mapItem coaItem="FPSS" statementType="CAS" lineID="880" precision="1">Issuance (Retirement) of Stock, Net</mapItem>
<mapItem coaItem="FPRD" statementType="CAS" lineID="970" precision="1">Issuance (Retirement) of Debt, Net</mapItem>
<mapItem coaItem="FTLF" statementType="CAS" lineID="980" precision="1">Cash from Financing Activities</mapItem>
<mapItem coaItem="SFEE" statementType="CAS" lineID="990" precision="1">Foreign Exchange Effects</mapItem>
<mapItem coaItem="SNCC" statementType="CAS" lineID="1000" precision="1">Net Change in Cash</mapItem>
<mapItem coaItem="SCIP" statementType="CAS" lineID="1040" precision="1">Cash Interest Paid</mapItem>
<mapItem coaItem="SCTP" statementType="CAS" lineID="1050" precision="1">Cash Taxes Paid</mapItem>
</COAMap>
"""

FieldInfo = namedtuple('FieldInfo', ['statementType', 'lineID', 'precision', 'name'])
fields_map = {}
root = ET.fromstring(xml_string)
for item in root.getchildren():
    code = item.attrib['coaItem']
    statementType = item.attrib['statementType']
    lineID = item.attrib['lineID']
    precision = item.attrib['precision']
    name = item.text
    fields_map[code] = FieldInfo(statementType, lineID, precision, name)

# print(fields_map)
