from flask import request, jsonify, url_for

from app import db
from app.api import api
from ..postgres.__all_models import Contract


# @api.route('/', methods=['GET'])
# def get_base():
#     return 'from api'


@api.route('/contracts', methods=['GET'])
def get_contracts():
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = Contract.query.paginate(
        page, per_page=50,
        error_out=False)
    contracts = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_contracts', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_contracts', page=page + 1)
    return jsonify({
        'contracts': [contract.to_json() for contract in contracts],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/contracts', methods=['POST'])
def contract_post():
    contract = Contract.from_json(request.json)
    if Contract.query.filter_by(conId=contract.conId).first():
        return jsonify({'error': 'contract already in database', 'contract': contract.conId}), 400
    db.session.add(contract)
    db.session.commit()
    return jsonify(contract.to_json()), 201, \
           {'Location': url_for('api.get_contract', con_id=contract.conId)}


@api.route('/contracts/<string:con_id>', methods=['GET'])
def get_contract(con_id):
    contract = Contract.query.get_or_404(con_id)
    return jsonify(contract.to_json())
