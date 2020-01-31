class Scope:
    def __init__(self, stocks=None, exchanges=None):
        if stocks:
            self.stocks = (stock for stock in stocks)
            self.mode = 'stocks'
        if exchanges:
            self.exchanges = (exchange for exchange in exchanges)
            self.mode = 'exchanges'

    @property
    def Perimeter(self):
        if self.mode == 'stocks':
            return self.mode, self.stocks
        if self.mode == 'exchanges':
            return self.mode, self.exchanges