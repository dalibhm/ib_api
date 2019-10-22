import datetime
import uuid
import mongoengine


class Statement(mongoengine.Document):
    ticker = mongoengine.StringField(required=True)
    last_modified = mongoengine.DateField(required=True)
    statement_type = mongoengine.StringField(required=True)
    fiscal_period = mongoengine.MapField(field=mongoengine.StringField())
    update_type = mongoengine.StringField(required=True)
    statement_date = mongoengine.DateField(required=True)
    auditor_name = mongoengine.StringField()
    auditor_opinion = mongoengine.StringField()
    source = mongoengine.StringField(required=True)
    source_date = mongoengine.DateField(required=True)
    statement = mongoengine.MapField(field=mongoengine.FloatField())
    insert_date = mongoengine.DateTimeField(default=datetime.datetime.now)


    meta = {
        'db_alias': 'core',
        'collection': 'FinancialStatements',
    }