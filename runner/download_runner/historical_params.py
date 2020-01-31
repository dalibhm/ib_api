from injector import inject


class HistoricalParams:
    @inject
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
