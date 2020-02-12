import mongoengine
from mongo_data.statement import Statement


class MongoRepository:

    @staticmethod
    def process_report(symbol, report_type, report_content):
        report_content = report_content.replace('\r', '')
        latest = Statement.objects(ticker=symbol, report_type=report_type, report=report_content).first()
        if latest and latest.report == report_content:
            return
        statement_record = Statement(ticker=symbol, report_type=report_type, report=report_content)
        statement_record.save()

    @staticmethod
    def get_all_reports(symbol, report_type):
        reports = Statement.objects(ticker=symbol, report_type=report_type).all()
        return reports

    @staticmethod
    def get_latest_report(symbol, report_type):
        reports = Statement.objects(ticker=symbol, report_type=report_type).first()
        return reports

    @staticmethod
    def get_latest_report_date(symbol, report_type):
        pass
