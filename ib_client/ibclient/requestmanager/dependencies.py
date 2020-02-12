from injector import singleton


class HistoricalDependencies:
    def __init__(self):
        pass

    def configuration(self, binder):
        binder.bind(HistoricalDataProcessor, to=self.config, scope=singleton)
        binder.bind(FundamentalDataProcessor, to=self.config, scope=singleton)