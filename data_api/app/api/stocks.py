from flask import request, jsonify, url_for

from app import db
from ..postgres.__all_models import Stock
from app.api import api


@api.route('/stocks', methods=['GET'])
def get_stocks():
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = Stock.query.paginate(
        page, per_page=50,
        error_out=False)
    stocks = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_stocks', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_stocks', page=page + 1)
    return jsonify({
        'stocks': [stock.to_json() for stock in stocks],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/stocks', methods=['POST'])
def post_stock():
    stock = Stock.from_json(request.json)
    if Stock.query.filter_by(con_id=stock.con_id).first():
        return jsonify({'error': 'contract already in database', 'contract': stock.con_id}), 400
    db.session.add(stock)
    db.session.commit()
    return jsonify(stock.to_json()), 201, \
           {'Location': url_for('api.get_stock_by_con_id', con_id=stock.con_id)}


@api.route('/stocks/id/<string:con_id>', methods=['GET'])
def get_stock_by_con_id(con_id):
    contract = Stock.query.get_or_404(con_id)
    return jsonify(contract.to_json())


@api.route('/stocks/symbol/<string:symbol>', methods=['GET'])
def get_stock_by_symbol(symbol):
    contract = Stock.query.filter_by(symbol=symbol).first()
    return jsonify(contract.to_json())
