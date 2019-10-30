from flask import request, jsonify, url_for, Blueprint
from app import db

from ..postgres.BarData import BarData

historical_data_blueprint = Blueprint('historical_data', __name__)


# @historical_data_blueprint.route('/<stock>/<what_to_show>/<as_of_date>', methods=['GET'])
# def get_historical_data_point(stock, what_to_show, as_of_date):
#     historical_data_point = BarData.query(symbol=stock, whatToShow=what_to_show, date=as_of_date).to
#     return jsonify({
#         'historical_data': [point.to_json() for point in historical_data_point],
#     })


@historical_data_blueprint.route('/<stock>/<what_to_show>', methods=['GET'])
def get_historical_data_for_stock(stock, what_to_show):
    # return 'from comments'
    page = request.args.get('page', 1, type=int)
    pagination = BarData.query(symbol=stock, whatToShow=what_to_show).paginate(
        page, per_page=50,
        error_out=False)
    historical_data = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_historical_data_for_stock', page=page - 1)
    next = None
    if pagination.has_next:
        next = url_for('api.get_historical_data_for_stock', page=page + 1)
    return jsonify({
        'historical_data': [bar_data.to_json() for bar_data in historical_data],
        'prev': prev,
        'next': next,
        'count': pagination.total
    })


@historical_data_blueprint.route('/', methods=['POST'])
def historical_data_post():
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
                                stock=bar_data.symbol, whatToShow=bar_data.whatToShow, date=bar_data.date)}


@historical_data_blueprint.route('/<string:stock>/<string:whatToShow>/<string:date>', methods=['GET'])
def get_historical_point(stock, whatToShow, date):
    bar_data = BarData.query.filter_by(symbol=stock, whatToShow=whatToShow, date=date).first()
    return jsonify(bar_data.to_json())
