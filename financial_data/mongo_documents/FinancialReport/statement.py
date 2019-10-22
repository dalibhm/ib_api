import datetime
import uuid
import mongoengine

from mongo_documents.FinancialReport.CommonFields import CodedField


class FiscalPeriod(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    end_date = mongoengine.StringField(required=True)
    fiscal_year = mongoengine.StringField(required=True)
    fiscal_period_number = mongoengine.StringField()

    def __str__(self):
        if self.fiscal_period_number is None:
            return '{} . {} . {}'.format(self.type, self.end_date, self.fiscal_year)
        return '{} . {} . {}.Q{}'.format(self.type, self.end_date, self.fiscal_year, self.fiscal_period_number)


class StatementInfo(mongoengine.EmbeddedDocument):
    period_length = mongoengine.IntField()
    # add coded field here
    period_type = mongoengine.EmbeddedDocumentField(CodedField)
    update_type = mongoengine.EmbeddedDocumentField(CodedField, required=True)
    accounting_std = mongoengine.StringField()
    statement_date = mongoengine.DateField(required=True)
    auditor_name = mongoengine.EmbeddedDocumentField(CodedField)
    auditor_opinion = mongoengine.EmbeddedDocumentField(CodedField)
    source = mongoengine.StringField(required=True)
    source_date = mongoengine.DateField(required=True)

    def __str__(self):
        return '{} {}'.format(self.period_type, self.source, self.source_date)


class Statement(mongoengine.Document):
    ticker = mongoengine.StringField(required=True,
                                     unique_with=['fiscal_period.end_date', 'fiscal_period.type', 'type'])
    # add statement info id reference
    fiscal_period = mongoengine.EmbeddedDocumentField(FiscalPeriod, required=True)
    statement_info = mongoengine.EmbeddedDocumentField(StatementInfo, required=True)
    type = mongoengine.StringField(required=True)
    statement = mongoengine.MapField(field=mongoengine.FloatField())
    insert_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'FinancialStatements',
        'indexes': [
            'ticker', 'fiscal_period.end_date', 'fiscal_period.type',
            {'fields': ['ticker', 'fiscal_period.end_date', 'fiscal_period.type']}
        ]
    }

    def __str__(self):
        out = 'ticker: {}'.format(self.ticker)
        out = '{}\nfiscal_period: {}'.format(out, self.fiscal_period)
        out = '{}\nstatement_info: {}'.format(out, self.statement_info)
        out = '{}\ntype: {}'.format(out, self.type)
        out = '{}\nstatement: {}'.format(out, self.statement)
        out = '{}\ninsert_date: {}'.format(out, self.insert_date)
        return '{}\n'.format(out)
