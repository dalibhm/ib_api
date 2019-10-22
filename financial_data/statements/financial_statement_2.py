class CompanyId:
    def __init__(self, field, value):
        self.field = field
        self.value = value

 class Exchange:
        def __init__(self, code, name, country):
            self.code = code
            self.country = country
            self.name = name

class Issue:
    def __init__(self, _id, _type, _description, _order, _issue_ids, exchange_code, exchange_name):
        self.id = _id
        self.type = _type
        self.description = _description
        self.order = _order
        self.issue_ids = _issue_ids
        self.exchange = Exchange(exchange_code, exchange_country)

class CompanyInfo:
    def __init__(self):
        pass

class StatementInfo:
    def __init__(self):
        pass

class Notes:
    def __init__(self):
        pass





