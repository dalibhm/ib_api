import datetime
from enum import Enum
from dateutil.relativedelta import relativedelta

# Type	Open	High	Low	Close	Volume
# TRADES	First traded price	Highest traded price	Lowest traded price	Last traded price	Total traded volume
# MIDPOINT	Starting midpoint price	Highest midpoint price	Lowest midpoint price	Last midpoint price	N/A
# BID	Starting bid price	Highest bid price	Lowest bid price	Last bid price	N/A
# ASK	Starting ask price	Highest ask price	Lowest ask price	Last ask price	N/A
# BID_ASK	Time average bid	Max Ask	Min Bid	Time average ask	N/A
# ADJUSTED_LAST	Dividend-adjusted first traded price	Dividend-adjusted high trade	Dividend-adjusted low trade	Dividend-adjusted last trade	Total traded volume
# HISTORICAL_VOLATILITY	Starting volatility	Highest volatility	Lowest volatility	Last volatility	N/A
# OPTION_IMPLIED_VOLATILITY	Starting implied volatility	Highest implied volatility	Lowest implied volatility	Last implied volatility	N/A
# REBATE_RATE	Starting rebate rate	Highest rebate rate	Lowest rebate rate	Last rebate rate	N/A
# FEE_RATE	Starting fee rate	Highest fee rate	Lowest fee rate	Last fee rate	N/A
# YIELD_BID	Starting bid yield	Highest bid yield	Lowest bid yield	Last bid yield	N/A
# YIELD_ASK	Starting ask yield	Highest ask yield	Lowest ask yield	Last ask yield	N/A
# YIELD_BID_ASK	Time average bid yield	Highest ask yield	Lowest bid yield	Time average ask yield	N/A
# YIELD_LAST	Starting last yield	Highest last yield	Lowest last yield	Last last yield
# N/A

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


class HistoricalRequest:
    def __init__(self, start_date: str, end_date: str, bar_size='1 day', price_type: PriceType = PriceType.ADJUSTED_LAST):
        self.start_date = datetime.datetime.strptime(start_date, '%Y%m%d')
        self.end_date = datetime.datetime.strptime(end_date, '%Y%m%d')
        self.bar_size = bar_size
        self.price_type = price_type
        period_length = relativedelta(self.end_date, self.start_date)
        if period_length.years > 0:
            self.period_length = period_length.years
            self.period_unit = 'Y'
        elif period_length.months > 0:
            self.period_length = period_length.months
            self.period_unit = 'M'
        else:
            self.period_length = period_length.days
            self.period_unit = 'D'

    def request_args(self):
        return {'end_date_time': self.end_date,
                'historical_data_length': '{} {}'.format(self.period_length, self.period_unit),
                'bar_size': self.bar_size,
                'price_type': self.price_type.name
                }
