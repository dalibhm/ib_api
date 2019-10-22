from mongo_documents.FinancialSummary.financial_summary import FinancialSummary
from mongo_setup import global_init
from mongo_documents.FinancialReport.financial_statement_info import FinancialStatementInfo
from mongo_documents.FinancialReport.statement import Statement

global_init()


def write_financial_statement(record: Statement):
    look_for_record = Statement.objects().filter(ticker=record.ticker,
                                                 fiscal_period__end_date=record.fiscal_period.end_date,
                                                 fiscal_period__type__=record.fiscal_period.type,
                                                 type=record.type).limit(1)
    if not look_for_record:
        record.save()


def write_financial_statement_info(record: FinancialStatementInfo, ticker):
    look_for_ticker = FinancialStatementInfo.objects().filter(ticker=ticker)
    if not look_for_ticker:
        record.save()

        summary_record = FinancialSummary(ticker=ticker,
                                          currency=currency,
                                          data_type=field,
                                          as_of_date=record.attrib['asofDate'],
                                          report_type=record.attrib['reportType'],
                                          period=record.attrib['period'],
                                          value=float(record.text)
                                          )


def write_financial_summary(record: FinancialSummary):
    look_for_record = FinancialSummary.objects().filter(ticker=record.ticker,
                                                        data_type=record.data_type,
                                                        as_of_date=record.as_of_date,
                                                        period=record.period).limit(1)
