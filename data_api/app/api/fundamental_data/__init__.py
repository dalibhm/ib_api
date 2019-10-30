from flask import Blueprint

fundamental_data_blueprint = Blueprint('fundamental_data', __name__)

from . import financial_reports as financial_reports
from . import fundamental_raw_xmls as fundamental_raw_xmls
# from . import financial_summaries as financial_summaries
