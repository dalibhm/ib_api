import os
import sys


module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))

# {'conId': 13181, 'symbol': 'AEE', 'secType': 'STK', 'lastTradeDateOrContractMonth': '', 'strike': 0.0, 'right': '', 'multiplier': '', 'exchange': 'AMEX', 'primaryExchange': 'NYSE', 'currency': 'USD', 'localSymbol': 'AEE', 'tradingClass': 'AEE', 'includeExpired': False, 'secIdType': '', 'secId': '', 'comboLegsDescrip': '', 'comboLegs': None, 'deltaNeutralContract': None}
#
#
contract_details_sample = {
    'contractId': 13181,
    'marketName': 'AEE',
    'minTick': 0.01,
    'orderTypes': 'ACTIVETIM,ADJUST,ALERT,ALLOC,AVGCOST,BASKET,BENCHPX,COND,CONDORDER,DAY,DEACT,DEACTDIS,DEACTEOD,GAT,GTC,GTD,GTT,HID,IOC,LIT,LMT,LOC,MIT,MKT,MOC,MTL,NGCOMB,NONALGO,OCA,OPG,PEGBENCH,PEGMID,POSTONLY,RTH,SCALE,SCALERST,SNAPMID,SNAPMKT,SNAPREL,STP,STPLMT,TRAIL,TRAILLIT,TRAILLMT,TRAILMIT,WHATIF',
    'validExchanges': 'SMART,AMEX,NYSE,CBOE,PHLX,ISE,CHX,ARCA,ISLAND,DRCTEDGE,BEX,BATS,EDGEA,CSFBALGO,JEFFALGO,BYX,IEX,EDGX,FOXRIVER,TPLUS1,NYSENAT,PSX',
    'priceMagnifier': 1,
    'underConId': 0,
    'longName': 'AMEREN CORP',
    'contractMonth': '',
    'industry': 'Utilities',
    'category': 'Electric',
    'subcategory': 'Electric-Integrated',
    'timeZoneId': 'EST5EDT',
    'tradingHours': '20200101:CLOSED;20200102:0700-20200102:2000;20200103:0700-20200103:2000;20200104:CLOSED;20200105:CLOSED;20200106:0700-20200106:2000;20200107:0700-20200107:2000;20200108:0700-20200108:2000;20200109:0700-20200109:2000;20200110:0700-20200110:2000;20200111:CLOSED;20200112:CLOSED;20200113:0700-20200113:2000;20200114:0700-20200114:2000;20200115:0700-20200115:2000;20200116:0700-20200116:2000;20200117:0700-20200117:2000;20200118:CLOSED;20200119:CLOSED;20200120:0700-20200120:2000;20200121:0700-20200121:2000;20200122:0700-20200122:2000;20200123:0700-20200123:2000;20200124:0700-20200124:2000;20200125:CLOSED;20200126:CLOSED;20200127:0700-20200127:2000;20200128:0700-20200128:2000;20200129:0700-20200129:2000;20200130:0700-20200130:2000;20200131:0700-20200131:2000;20200201:CLOSED;20200202:CLOSED;20200203:0700-20200203:2000;20200204:0700-20200204:2000', 'liquidHours': '20200101:CLOSED;20200102:0930-20200102:1600;20200103:0930-20200103:1600;20200104:CLOSED;20200105:CLOSED;20200106:0930-20200106:1600;20200107:0930-20200107:1600;20200108:0930-20200108:1600;20200109:0930-20200109:1600;20200110:0930-20200110:1600;20200111:CLOSED;20200112:CLOSED;20200113:0930-20200113:1600;20200114:0930-20200114:1600;20200115:0930-20200115:1600;20200116:0930-20200116:1600;20200117:0930-20200117:1600;20200118:CLOSED;20200119:CLOSED;20200120:0930-20200120:1600;20200121:0930-20200121:1600;20200122:0930-20200122:1600;20200123:0930-20200123:1600;20200124:0930-20200124:1600;20200125:CLOSED;20200126:CLOSED;20200127:0930-20200127:1600;20200128:0930-20200128:1600;20200129:0930-20200129:1600;20200130:0930-20200130:1600;20200131:0930-20200131:1600;20200201:CLOSED;20200202:CLOSED;20200203:0930-20200203:1600;20200204:0930-20200204:1600',
    'evRule': '',
    'evMultiplier': 0,
    'mdSizeMultiplier': 100,
    'aggGroup': 1,
    'underSymbol': '',
    'underSecType': '',
    'marketRuleIds': '26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26',
    'secIdList': None,
    'realExpirationDate': '',
    'lastTradeTime': '',
    'cusip': '',
    'ratings': '',
    'descAppend': '',
    'bondType': '',
    'couponType': '',
    'callable': False,
    'putable': False,
    'coupon': 0,
    'convertible': False,
    'maturity': '',
    'issueDate': '',
    'nextOptionDate': '',
    'nextOptionType': '',
    'nextOptionPartial': False,
    'notes': ''
}

