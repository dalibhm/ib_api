from flask import request, jsonify, url_for

from app import db
from ..postgres.__all_models import Exchange
from app.api import api


@api.route('/exchanges', methods=['GET'])
def get_exchanges():
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = Exchange.query.paginate(
        page, per_page=50,
        error_out=False)
    exchanges = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_exchanges', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_exchanges', page=page + 1)
    return jsonify({
        'exchanges': [exchange.to_json() for exchange in exchanges],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/exchanges', methods=['POST'])
def post_exchange():
    exchange = Exchange.from_json(request.json)
    if exchange.query.filter_by(name=exchange.name).first():
        return jsonify({'error': 'contract already in database', 'contract': exchange.name}), 400
    db.session.add(exchange)
    db.session.commit()
    return jsonify(exchange.to_json()), 201, \
           {'Location': url_for('api.get_exchange', code=exchange.code)}


@api.route('/exchanges/<string:code>', methods=['GET'])
def get_exchange(code):
    contract = Exchange.query.get_or_404(code)
    return jsonify(contract.to_json())
