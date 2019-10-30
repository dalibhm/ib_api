from datetime import datetime

from app.exceptions import ValidationError
import sqlalchemy
from app import db


class FinancialStatement(db.Model):
    __tablename__ = "fundamental_statements"

    symbol = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    report_type = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    xml = sqlalchemy.Column(sqlalchemy.String)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, primary_key=True)
    report_date = sqlalchemy.Column(sqlalchemy.DateTime)

    @staticmethod
    def from_json(json_statement):
        # body = json_contract.get('body')
        try:
            return FinancialStatement(**json_statement)
        except:
            raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_statement = {
            'symbol': self.symbol,
            'report_type': self.report_type,
            'xml': self.xml,
            'insert_date': self.insert_date,
            'report_date': self.report_date
        }
        return json_statement


class FinancialSummary(db.Model):
    __tablename__ = "financial_summaries"

    symbol = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    xml = sqlalchemy.Column(sqlalchemy.String)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, primary_key=True)
    report_date = sqlalchemy.Column(sqlalchemy.DateTime)

    @staticmethod
    def from_json(json_statement):
        # body = json_contract.get('body')
        try:
            return FinancialStatement(**json_statement)
        except:
            raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_statement = {
            'symbol': self.symbol,
            'xml': self.xml,
            'insert_date': self.insert_date,
            'report_date': self.report_date
        }
        return json_statement


class FinancialSnapshot(db.Model):
    __tablename__ = "financial_snapshots"

    symbol = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    xml = sqlalchemy.Column(sqlalchemy.String)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, primary_key=True)
    report_date = sqlalchemy.Column(sqlalchemy.DateTime)

    @staticmethod
    def from_json(json_statement):
        # body = json_contract.get('body')
        try:
            return FinancialStatement(**json_statement)
        except:
            raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_statement = {
            'symbol': self.symbol,
            'xml': self.xml,
            'insert_date': self.insert_date,
            'report_date': self.report_date
        }
        return json_statement


class OwnershipReport(db.Model):
    __tablename__ = "ownership_reports"

    symbol = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    xml = sqlalchemy.Column(sqlalchemy.String)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, primary_key=True)
    report_date = sqlalchemy.Column(sqlalchemy.DateTime)

    @staticmethod
    def from_json(json_statement):
        # body = json_contract.get('body')
        try:
            return FinancialStatement(**json_statement)
        except:
            raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_statement = {
            'symbol': self.symbol,
            'xml': self.xml,
            'insert_date': self.insert_date,
            'report_date': self.report_date
        }
        return json_statement


class CalendarReport(db.Model):
    __tablename__ = "calendar_reports"

    symbol = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    xml = sqlalchemy.Column(sqlalchemy.String)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, primary_key=True)
    report_date = sqlalchemy.Column(sqlalchemy.DateTime)

    @staticmethod
    def from_json(json_statement):
        # body = json_contract.get('body')
        try:
            return FinancialStatement(**json_statement)
        except:
            raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_statement = {
            'symbol': self.symbol,
            'xml': self.xml,
            'insert_date': self.insert_date,
            'report_date': self.report_date
        }
        return json_statement


class EariningEstimateReport(db.Model):
    __tablename__ = "earning_estimate_reports"

    symbol = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    xml = sqlalchemy.Column(sqlalchemy.String)
    insert_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now, primary_key=True)
    report_date = sqlalchemy.Column(sqlalchemy.DateTime)

    @staticmethod
    def from_json(json_statement):
        # body = json_contract.get('body')
        try:
            return FinancialStatement(**json_statement)
        except:
            raise ValidationError('Contract cannot be constructed')

    def to_json(self):
        json_statement = {
            'symbol': self.symbol,
            'xml': self.xml,
            'insert_date': self.insert_date,
            'report_date': self.report_date
        }
        return json_statement
