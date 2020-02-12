import datetime
import uuid
import mongoengine
from proto.fundamental_data_pb2 import Report


class Statement(mongoengine.Document):
    ticker = mongoengine.StringField(required=True)
    insert_date = mongoengine.DateTimeField(required=True, default=datetime.datetime.now)
    report_type = mongoengine.StringField(required=True)
    report = mongoengine.StringField(required=True)

    meta = {
        'db_alias': 'financialDataRepository',
        'collection': 'financialDataRepository',
        'ordering': ['-insert_date'],
        'indexes': [
            'ticker', 'insert_date', 'report_type',
            {'fields': ['ticker', 'report_type', 'insert_date']}
        ]
    }

    def __str__(self):
        return '{} . {} . {}'.format(self.ticker, self.insert_date, self.report_type)

    def to_proto(self):
        report = Report(stock=self.ticker,
                        reportType=self.report_type,
                        content=self.report,
                        insertDate=self.insert_date.strftime("%m/%d/%Y, %H:%M:%S"))
        return report
