import datetime

import mongoengine


class Earnings(mongoengine.EmbeddedDocument):
    q1 = mongoengine.DateField(required=True)
    q2 = mongoengine.DateField(required=True)
    q3 = mongoengine.DateField(required=True)
    q4 = mongoengine.DateField(required=True)
    period = mongoengine.StringField(required=True)
    time = mongoengine.StringField(required=True)
    etype = mongoengine.StringField(required=True)
    date = mongoengine.DateField(required=True)
    timestamp = mongoengine.DateTimeField(required=True)


class EarningsCallTranscript(mongoengine.EmbeddedDocument):
    period = mongoengine.StringField(required=True)
    url = mongoengine.StringField(required=True)
    timestamp = mongoengine.DateTimeField(required=True)


class ShareHolderMeeting(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    date = mongoengine.DateField(required=True)
    timestamp = mongoengine.DateTimeField(required=True)


class CalendarReport(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField(required=True)
    ticker = mongoengine.StringField(required=True, unique=True)
    ISIN = mongoengine.StringField(required=True)
    exchange = mongoengine.StringField(required=True)
    country = mongoengine.StringField(required=True)
    conids = mongoengine.ListField(field=mongoengine.IntField)
    earnings = mongoengine.EmbeddedDocumentFieldList(Earnings, required=True)
    earning_calls_transcripts = mongoengine.EmbeddedDocumentFieldList(EarningsCallTranscript, required=True)
    shareholder_meetings = mongoengine.EmbeddedDocumentFieldList(ShareHolderMeeting, required=True)
    insert_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'FinancialSummaries',
        'indexes': [
            'ticker', 'exchange'
        ]
    }
