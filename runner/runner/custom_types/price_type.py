from enum import Enum


class PriceType(Enum):
    TRADES = 1
    MIDPOINT = 2
    BID = 3
    ASK = 4
    BID_ASK = 5
    ADJUSTED_LAST = 6
    HISTORICAL_VOLATILITY = 7
    OPTION_IMPLIED_VOLATILITY = 8
    REBATE_RATE = 9
    FEE_RATE = 10
    YIELD_BID = 11
    YIELD_ASK = 12
    YIELD_BID_ASK = 13
    YIELD_LAST = 14