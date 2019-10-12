import mongoengine


class Stock(mongoengine.Document):
    con_id = mongoengine.IntField(required=True, unique=True)
    ib_symbol = mongoengine.StringField(required=True, unique=True)
    # add statement info id reference
    currency = mongoengine.StringField(required=True)
    symbol = mongoengine.StringField(required=True, unique=True)
    exchange = mongoengine.StringField(required=True)
    product_description_link = mongoengine.StringField(required=True)


    meta = {
        'db_alias': 'core',
        'collection': 'ib_stocks',
        'indexes': [
            'con_id', 'ib_symbol', 'symbol', 'currency', 'exchange'
        ]
    }