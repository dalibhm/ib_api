class FinancialStatement:
    def __init__(self, coIds, Issues, CoGeneralInfo, StatementInfo, Notes, FinancialStatements):
        self.coIds = coIds
        self.Issues = Issues
        self.CoGeneralInfo = CoGeneralInfo
        self.StatementInfo = StatementInfo
        self.Notes = Notes
        self.FinancialStatements = FinancialStatements


class Statement:
    def __init__(self, statement_type, fiscal_period, statement_period, statement_info, statement_data):
        self.statement_type = statement_type
        self.fiscal_period = fiscal_period
        self.statement_period = statement_period
        self.statement_info = statement_info
        self.statement_data = statement_data


class StatementInfo:
    def __init__(self):
        self.PeriodLength = None
        self.UpdateType = None
        self.AccountingStd = None
        self.StatementDate = None
        self.AuditorCode = None
        self.AuditorName = None
        self.AuditorOpinion = None
        self.Source = None
        self.SourceDate = None

        < PeriodLength > 12 < / PeriodLength >
        < UpdateType
        Code = "UPD" > Updated
        Normal < / UpdateType >
        < AccountingStd > < / AccountingStd >
        < StatementDate > 2017 - 12 - 31 < / StatementDate >
        < AuditorName
        Code = "GTTT" > Grant
        Thornton
        LLP < / AuditorName >
        < AuditorOpinion
        Code = "UNQ" > Unqualified < / AuditorOpinion >
        < Source
        Date = "2018-02-15" > 10 - K < / Source >

class StatementData:
    def __init__(self):
        self.fields = []
        self.values = []

    def read_field(self, field, value):
        self.fields.append(field)
        self.values.append(field)