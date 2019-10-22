import mongoengine


class CodedField(mongoengine.EmbeddedDocument):
    code = mongoengine.StringField(required=True)
    value = mongoengine.StringField(required=True)