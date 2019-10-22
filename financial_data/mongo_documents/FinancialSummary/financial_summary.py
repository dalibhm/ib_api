import datetime

import mongoengine


class FinancialSummary(mongoengine.Document):
    ticker = mongoengine.StringField(required=True, unique_with=['data_type', 'as_of_date', 'period'])
    currency = mongoengine.StringField(required=True)
    data_type = mongoengine.StringField(required=True)
    as_of_date = mongoengine.DateField(required=True)
    report_type = mongoengine.StringField(required=True)
    period = mongoengine.StringField(required=True)
    value = mongoengine.FloatField(required=True)
    insert_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'FinancialSummaries',
        'indexes': [
            'ticker', 'data_type', 'as_of_date',
            {'fields': ['ticker', 'data_type', 'as_of_date', 'period']}
        ]
    }
