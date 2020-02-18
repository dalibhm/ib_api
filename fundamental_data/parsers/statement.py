class Statement:

    fields = ["SREV",  # statementType="INC" lineID="100" precision="1">Revenue</mapItem>
    "SORE" ,  #statementType="INC" lineID="300" precision="1">Other Revenue, Total</mapItem>
    "RTLR" ,  #statementType="INC" lineID="310" precision="1">Total Revenue</mapItem>
    "SCOR" ,  #statementType="INC" lineID="360" precision="1">Cost of Revenue, Total</mapItem>
    "SGRP" ,  #statementType="INC" lineID="370" precision="1">Gross Profit</mapItem>
    "SSGA" ,  #statementType="INC" lineID="550" precision="1">Selling/General/Admin. Expenses, Total</mapItem>
    "ERAD" ,  #statementType="INC" lineID="560" precision="1">Research &amp; Development</mapItem>
    "SDPR" ,  #statementType="INC" lineID="600" precision="1">Depreciation/Amortization</mapItem>
    "SINN" ,  #statementType="INC" lineID="671" precision="1">Interest Exp.(Inc.),Net-Operating, Total</mapItem>
    "SUIE" ,  #statementType="INC" lineID="740" precision="1">Unusual Expense (Income)</mapItem>
    "SOOE" ,  #statementType="INC" lineID="820" precision="1">Other Operating Expenses, Total</mapItem>
    "ETOE" ,  #statementType="INC" lineID="830" precision="1">Total Operating Expense</mapItem>
    "SOPI" ,  #statementType="INC" lineID="840" precision="1">Operating Income</mapItem>
    "SNIN" ,  #statementType="INC" lineID="911" precision="1">Interest Inc.(Exp.),Net-Non-Op., Total</mapItem>
    "NGLA" ,  #statementType="INC" lineID="920" precision="1">Gain (Loss) on Sale of Assets</mapItem>
    "SONT" ,  #statementType="INC" lineID="1270" precision="1">Other, Net</mapItem>
    "EIBT" ,  #statementType="INC" lineID="1280" precision="1">Net Income Before Taxes</mapItem>
    "TTAX" ,  #statementType="INC" lineID="1290" precision="1">Provision for Income Taxes</mapItem>
    "TIAT" ,  #statementType="INC" lineID="1300" precision="1">Net Income After Taxes</mapItem>
    "CMIN" ,  #statementType="INC" lineID="1310" precision="1">Minority Interest</mapItem>
    "CEIA" ,  #statementType="INC" lineID="1320" precision="1">Equity In Affiliates</mapItem>
    "CGAP" ,  #statementType="INC" lineID="1330" precision="1">U.S. GAAP Adjustment</mapItem>
    "NIBX" ,  #statementType="INC" lineID="1340" precision="1">Net Income Before Extra. Items</mapItem>
    "STXI" ,  #statementType="INC" lineID="1390" precision="1">Total Extraordinary Items</mapItem>
    "NINC" ,  #statementType="INC" lineID="1400" precision="1">Net Income</mapItem>
    "SANI" ,  #statementType="INC" lineID="1460" precision="1">Total Adjustments to Net Income</mapItem>
    "CIAC" ,  #statementType="INC" lineID="1470" precision="1">Income Available to Com Excl ExtraOrd</mapItem>
    "XNIC" ,  #statementType="INC" lineID="1480" precision="1">Income Available to Com Incl ExtraOrd</mapItem>
    "SDAJ" ,  #statementType="INC" lineID="1520" precision="1">Dilution Adjustment</mapItem>
    "SDNI" ,  #statementType="INC" lineID="1530" precision="1">Diluted Net Income</mapItem>
    "SDWS" ,  #statementType="INC" lineID="1540" precision="2">Diluted Weighted Average Shares</mapItem>
    "SDBF" ,  #statementType="INC" lineID="1550" precision="3">Diluted EPS Excluding ExtraOrd Items</mapItem>
    "DDPS1",  # statementType="INC" lineID="1570" precision="3">DPS - Common Stock Primary Issue</mapItem>
    "VDES" ,  #statementType="INC" lineID="1770" precision="3">Diluted Normalized EPS</mapItem>
    "ACSH" ,  #statementType="BAL" lineID="10" precision="1">Cash</mapItem>
    "ACAE" ,  #statementType="BAL" lineID="20" precision="1">Cash &amp; Equivalents</mapItem>
    "ASTI" ,  #statementType="BAL" lineID="30" precision="1">Short Term Investments</mapItem>
    "SCSI" ,  #statementType="BAL" lineID="40" precision="1">Cash and Short Term Investments</mapItem>
    "AACR" ,  #statementType="BAL" lineID="70" precision="1">Accounts Receivable - Trade, Net</mapItem>
    "ATRC" ,  #statementType="BAL" lineID="100" precision="1">Total Receivables, Net</mapItem>
    "AITL" ,  #statementType="BAL" lineID="180" precision="1">Total Inventory</mapItem>
    "APPY" ,  #statementType="BAL" lineID="190" precision="1">Prepaid Expenses</mapItem>
    "SOCA" ,  #statementType="BAL" lineID="260" precision="1">Other Current Assets, Total</mapItem>
    "ATCA" ,  #statementType="BAL" lineID="270" precision="1">Total Current Assets</mapItem>
    "APTC" ,  #statementType="BAL" lineID="520" precision="1">Property/Plant/Equipment, Total - Gross</mapItem>
    "ADEP" ,  #statementType="BAL" lineID="530" precision="1">Accumulated Depreciation, Total</mapItem>
    "APPN" ,  #statementType="BAL" lineID="540" precision="1">Property/Plant/Equipment, Total - Net</mapItem>
    "AGWI" ,  #statementType="BAL" lineID="570" precision="1">Goodwill, Net</mapItem>
    "AINT" ,  #statementType="BAL" lineID="600" precision="1">Intangibles, Net</mapItem>
    "SINV" ,  #statementType="BAL" lineID="690" precision="1">Long Term Investments</mapItem>
    "ALTR" ,  #statementType="BAL" lineID="710" precision="1">Note Receivable - Long Term</mapItem>
    "SOLA" ,  #statementType="BAL" lineID="780" precision="1">Other Long Term Assets, Total</mapItem>
    "ATOT" ,  #statementType="BAL" lineID="880" precision="1">Total Assets</mapItem>
    "LAPB" ,  #statementType="BAL" lineID="890" precision="1">Accounts Payable</mapItem>
    "LPBA" ,  #statementType="BAL" lineID="900" precision="1">Payable/Accrued</mapItem>
    "LAEX" ,  #statementType="BAL" lineID="910" precision="1">Accrued Expenses</mapItem>
    "LSTD" ,  #statementType="BAL" lineID="1120" precision="1">Notes Payable/Short Term Debt</mapItem>
    "LCLD" ,  #statementType="BAL" lineID="1130" precision="1">Current Port. of  LT Debt/Capital Leases</mapItem>
    "SOCL" ,  #statementType="BAL" lineID="1220" precision="1">Other Current liabilities, Total</mapItem>
    "LTCL" ,  #statementType="BAL" lineID="1230" precision="1">Total Current Liabilities</mapItem>
    "LLTD" ,  #statementType="BAL" lineID="1240" precision="1">Long Term Debt</mapItem>
    "LCLO" ,  #statementType="BAL" lineID="1250" precision="1">Capital Lease Obligations</mapItem>
    "LTTD" ,  #statementType="BAL" lineID="1260" precision="1">Total Long Term Debt</mapItem>
    "STLD" ,  #statementType="BAL" lineID="1270" precision="1">Total Debt</mapItem>
    "SBDT" ,  #statementType="BAL" lineID="1300" precision="1">Deferred Income Tax</mapItem>
    "LMIN" ,  #statementType="BAL" lineID="1310" precision="1">Minority Interest</mapItem>
    "SLTL" ,  #statementType="BAL" lineID="1370" precision="1">Other Liabilities, Total</mapItem>
    "LTLL" ,  #statementType="BAL" lineID="1380" precision="1">Total Liabilities</mapItem>
    "SRPR" ,  #statementType="BAL" lineID="1410" precision="1">Redeemable Preferred Stock, Total</mapItem>
    "SPRS" ,  #statementType="BAL" lineID="1460" precision="1">Preferred Stock - Non Redeemable, Net</mapItem>
    "SCMS" ,  #statementType="BAL" lineID="1490" precision="1">Common Stock, Total</mapItem>
    "QPIC" ,  #statementType="BAL" lineID="1500" precision="1">Additional Paid-In Capital</mapItem>
    "QRED" ,  #statementType="BAL" lineID="1510" precision="1">Retained Earnings (Accumulated Deficit)</mapItem>
    "QTSC" ,  #statementType="BAL" lineID="1520" precision="1">Treasury Stock - Common</mapItem>
    "QEDG" ,  #statementType="BAL" lineID="1530" precision="1">ESOP Debt Guarantee</mapItem>
    "QUGL" ,  #statementType="BAL" lineID="1540" precision="1">Unrealized Gain (Loss)</mapItem>
    "SOTE" ,  #statementType="BAL" lineID="1590" precision="1">Other Equity, Total</mapItem>
    "QTLE" ,  #statementType="BAL" lineID="1600" precision="1">Total Equity</mapItem>
    "QTEL" ,  #statementType="BAL" lineID="1610" precision="1">Total Liabilities &amp; Shareholders' Equity</mapItem>
    "QTCO" ,  #statementType="BAL" lineID="1660" precision="2">Total Common Shares Outstanding</mapItem>
    "QTPO" ,  #statementType="BAL" lineID="1770" precision="2">Total Preferred Shares Outstanding</mapItem>
    "STBP" ,  #statementType="BAL" lineID="1980" precision="3">Tangible Book Value per Share, Common Eq</mapItem>
    "ONET" ,  #statementType="CAS" lineID="10" precision="1">Net Income/Starting Line</mapItem>
    "SDED" ,  #statementType="CAS" lineID="40" precision="1">Depreciation/Depletion</mapItem>
    "SAMT" ,  #statementType="CAS" lineID="80" precision="1">Amortization</mapItem>
    "OBDT" ,  #statementType="CAS" lineID="90" precision="1">Deferred Taxes</mapItem>
    "SNCI" ,  #statementType="CAS" lineID="170" precision="1">Non-Cash Items</mapItem>
    "SOCF" ,  #statementType="CAS" lineID="470" precision="1">Changes in Working Capital</mapItem>
    "OTLO" ,  #statementType="CAS" lineID="480" precision="1">Cash from Operating Activities</mapItem>
    "SCEX" ,  #statementType="CAS" lineID="520" precision="1">Capital Expenditures</mapItem>
    "SICF" ,  #statementType="CAS" lineID="670" precision="1">Other Investing Cash Flow Items, Total</mapItem>
    "ITLI" ,  #statementType="CAS" lineID="680" precision="1">Cash from Investing Activities</mapItem>
    "SFCF" ,  #statementType="CAS" lineID="730" precision="1">Financing Cash Flow Items</mapItem>
    "FCDP" ,  #statementType="CAS" lineID="760" precision="1">Total Cash Dividends Paid</mapItem>
    "FPSS" ,  #statementType="CAS" lineID="880" precision="1">Issuance (Retirement) of Stock, Net</mapItem>
    "FPRD" ,  #statementType="CAS" lineID="970" precision="1">Issuance (Retirement) of Debt, Net</mapItem>
    "FTLF" ,  #statementType="CAS" lineID="980" precision="1">Cash from Financing Activities</mapItem>
    "SFEE" ,  #statementType="CAS" lineID="990" precision="1">Foreign Exchange Effects</mapItem>
    "SNCC" ,  #statementType="CAS" lineID="1000" precision="1">Net Change in Cash</mapItem>
    "SCIP" ,  #statementType="CAS" lineID="1040" precision="1">Cash Interest Paid</mapItem>
    "SCTP" ]  #statementType="CAS" lineID="1050" precision="1">Cash Taxes Paid</mapItem>


    def __init__(self):
        pass

