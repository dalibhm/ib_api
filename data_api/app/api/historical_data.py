from flask import request, jsonify, url_for, Blueprint


from ..postgres.BarData import BarData

historical_data_blueprint = Blueprint('historical_data', __name__)


@historical_data_blueprint.route('/<stock>', methods=['GET'])
def get_stock(stock):
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = BarData.query(symbol=stock).paginate(
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


@historical_data_blueprint.route('/', methods=['POST'])
def contract_post():
    bar_data = BarData.from_json(request.json)
    if BarData.query. \
            filter_by(symbol=bar_data.symbol, whatToShow=bar_data.whatToShow, date=bar_data.date). \
            first():
        return jsonify({'error': 'contract already in database',
                        'data': bar_data.to_json(),
                        }), 400
    db.session.add(bar_data)
    db.session.commit()
    return jsonify(bar_data.to_json()), 201, \
           {'Location': url_for('historical_data.get_historical_point',
                                stock=bar_data.stock, whatToShow=bar_data.whatToShow, date=bar_data.date)}


@historical_data_blueprint.route('/<stock>/<whatToShow>/<date>', methods=['GET'])
def get_historical_point(stock, whatToShow, date):
    bar_data = BarData.query.get_or_404(stock=stock, whatToShow=whatToShow, date=date)
    return jsonify(bar_data.to_json())
