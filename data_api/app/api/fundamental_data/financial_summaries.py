from flask import request, jsonify, url_for

from app import db
from ...postgres.__all_models import FinancialSummary

from . import fundamental_data_blueprint


@fundamental_data_blueprint.route('financial_summaries', methods=['GET'])
def get_financial_summaries_stock_list():
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = FinancialSummary.query.paginate(
        page, per_page=50,
        error_out=False)
    statements = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('fundamental_data.get_financial_summaries_stock_list', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('fundamental_data.get_financial_summaries_stock_list', page=page + 1)
    return jsonify({
        'statements': [statement.symbol for statement in statements],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@fundamental_data_blueprint.route('financial_summaries/<stock>', methods=['GET'])
def get_financial_summaries_per_stock(stock):
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = FinancialSummary.query.filter_by(symbol=stock).paginate(
        page, per_page=1,
        error_out=False)
    statements = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('fundamental_data.get_financial_summaries_per_stock', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('fundamental_data.get_financial_summaries_per_stock', page=page + 1)
    return jsonify({
        'statements': [statement.to_json() for statement in statements],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@fundamental_data_blueprint.route('financial_summaries', methods=['POST'])
def post_financial_summary():
    statement = FinancialSummary.from_json(request.json)
    if FinancialSummary.query. \
            filter_by(symbol=statement.symbol). \
            first():
        return jsonify({'error': 'statement already in database',
                        'data': statement.to_json(),
                        }), 400
    db.session.add(statement)
    db.session.commit()
    return jsonify(statement.to_json()), 201, \
           {'Location': url_for('fundamental_data.get_financial_summary',
                                symbol=statement.symbol, report_date=statement.report_date)}


@fundamental_data_blueprint.route('financial_summaries/<symbol>/<report_date>', methods=['GET'])
def get_financial_summary(symbol, report_date):
    statement = FinancialSummary.query \
        .filter_by(symbol=symbol, report_date=report_date) \
        .first_or_404()

    return jsonify(statement.to_json())
