import mongoengine

from mongo_documents.FinancialReport.CommonFields import CodedField


class TypedField(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    value = mongoengine.StringField(required=True)


class Exchange(mongoengine.EmbeddedDocument):
    code = mongoengine.StringField(required=True)
    country = mongoengine.StringField(required=True)
    name = mongoengine.StringField(required=True)


class DatedIntField(mongoengine.EmbeddedDocument):
    date = mongoengine.DateField(required=True)
    value = mongoengine.IntField(required=True)


class Issue(mongoengine.EmbeddedDocument):
    id = mongoengine.StringField(required=True)
    type = mongoengine.StringField(required=True)
    desc = mongoengine.StringField(required=True)
    order = mongoengine.StringField(required=True)
    issue_ids = mongoengine.MapField(field=mongoengine.StringField())
    exchange = mongoengine.EmbeddedDocumentField(Exchange)
    most_recent_split = mongoengine.EmbeddedDocumentField(DatedIntField)


class GeneralInfo(mongoengine.EmbeddedDocument):
    company_status = mongoengine.EmbeddedDocumentField(CodedField)
    company_type = mongoengine.EmbeddedDocumentField(CodedField)
    last_modified = mongoengine.DateField(required=True)
    latest_available_annual = mongoengine.DateField(required=True)
    latest_available_interim = mongoengine.DateField(required=True)
    reporting_currency = mongoengine.EmbeddedDocumentField(CodedField)
    most_recent_exchange = mongoengine.EmbeddedDocumentField(DatedIntField)


class StatementInfo(mongoengine.EmbeddedDocument):
    coa_type = mongoengine.EmbeddedDocumentField(CodedField)
    balance_sheet_display = mongoengine.EmbeddedDocumentField(CodedField)
    cash_flow_method = mongoengine.EmbeddedDocumentField(CodedField)


class Notes(mongoengine.EmbeddedDocument):
    cfa_availability = mongoengine.StringField()
    i_availability = mongoengine.StringField()
    isi_availability = mongoengine.StringField()
    bsi_availability = mongoengine.StringField()
    cfi_availability = mongoengine.StringField()


class FinancialStatementInfo(mongoengine.Document):
    ticker = mongoengine.StringField(required=True, unique=True)
    company_ids = mongoengine.MapField(field=mongoengine.StringField(), required=True)
    issues = mongoengine.EmbeddedDocumentListField(Issue, required=True)
    general_info = mongoengine.EmbeddedDocumentField(GeneralInfo, required=True)
    statement_info = mongoengine.EmbeddedDocumentField(StatementInfo)
    notes = mongoengine.EmbeddedDocumentField(Notes)

    meta = {
        'db_alias': 'core',
        'collection': 'FinancialStatementsInfo',
        'indexes': [
            'ticker'
        ]
    }