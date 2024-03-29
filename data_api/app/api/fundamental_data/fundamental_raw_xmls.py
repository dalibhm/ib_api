import os
from datetime import datetime

from flask import request, jsonify, url_for

from app import db
from ...postgres.__all_models import FinancialStatement

from . import fundamental_data_blueprint


@fundamental_data_blueprint.route('xml', methods=['GET'])
# do something here
def get_fundamental_reports_stock_list():
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = FinancialStatement.query.paginate(
        page, per_page=50,
        error_out=False)
    statements = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('fundamental_data.get_fundamental_reports_stock_list', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('fundamental_data.get_fundamental_reports_stock_list', page=page + 1)
    return jsonify({
        'statements': [statement.symbol for statement in statements],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@fundamental_data_blueprint.route('xml/<stock>/<report>', methods=['GET'])
def get_xml_report_for_stock(stock, report):
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = FinancialStatement.query.filter_by(symbol=stock, report_type=report).paginate(
        page, per_page=1,
        error_out=False)
    statements = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('fundamental_data.get_xml_report_for_stock', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('fundamental_data.get_xml_report_for_stock', page=page + 1)
    return jsonify({
        'statements': [statement.to_json() for statement in statements],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@fundamental_data_blueprint.route('/xml', methods=['POST'])
def post_xml():
    data = request.json
    base_directory = 'data'
    filename = '{}_{}_{}.xml'.format(data['symbol'], data['report_type'], datetime.now())
    full_path = os.path.join('.', base_directory, filename)
    with open(full_path, "w") as file_writer:
        file_writer.write(data['xml'])
    return jsonify(data)


@fundamental_data_blueprint.route('financial_reports/<symbol>/<report_date>', methods=['GET'])
def get_financial_report(symbol, report_date):
    statement = FinancialStatement.query \
        .filter_by(symbol=symbol, report_date=report_date) \
        .first_or_404()

    return jsonify(statement.to_json())
