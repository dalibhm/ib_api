from flask import request, jsonify, url_for

from app import db
from app.api import api
from ..postgres.__all_models import ContractDetails


@api.route('/', methods=['GET'])
def get_base():
    return 'from api'


@api.route('/contracts/details', methods=['GET'])
def get_contract_details():
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = ContractDetails.query.paginate(
        page, per_page=50,
        error_out=False)
    contract_details = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_contract_details', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_contract_details', page=page + 1)
    return jsonify({
        'contract_details': [contract_detail.to_json() for contract_detail in contract_details],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@api.route('/contracts/details', methods=['POST'])
def post_contract_details():
    contract_details = ContractDetails.from_json(request.json)
    if ContractDetails.query.filter_by(contractId=contract_details.contractId).first():
        return jsonify({'error': 'contract_detail already in database', 'contract_detail': contract_details.contractId}) \
            , 400
    db.session.add(contract_details)
    db.session.commit()
    return jsonify(contract_details.to_json()), 201, \
           {'Location': url_for('api.get_contract_detail', con_id=contract_details.contractId)}


@api.route('/contracts/<string:con_id>/details/', methods=['GET'])
def get_contract_detail(con_id):
    contract_details = ContractDetails.query.get_or_404(con_id)
    return jsonify(contract_details.to_json())
