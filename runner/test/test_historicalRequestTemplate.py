import os
import sys

from download_runner.impl.historical_runner import HistoricalRunner
from request_templates.params import HistoricalRequestTemplate
from services.historical_data_service import HistoricalDataService

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '..'))


# from historical_data.historical_data_server import main as launch_historical_data_server
#
#
#
# @pytest.fixture(scope="module")
# def init():
#     launch_historical_data_server()
#     yield
#     time.sleep(1)


def test_historicalDataTemplate():
    params = {
        "start_date": "19990101",
        "end_date": "20191127",
        "bar_size": "1 day",
        "price_type": "TRADES"
    }
    request_template = HistoricalRequestTemplate(params)
    ib_params = request_template.params
    assert "20191127 00:00:00" == ib_params["endDateTime"]


def test_historicalDataTemplate_one_day_hist():
    params = {
        "start_date": "20191126",
        "end_date": "20191127",
        "bar_size": "1 day",
        "price_type": "TRADES"
    }
    request_template = HistoricalRequestTemplate(params)
    ib_parasms = request_template.params
    assert "20191127 00:00:00" == ib_parasms["endDateTime"]


def test_validate_params(monkeypatch):
    def mock_hist_request(*args, **kwargs):
        return True

    def mock_no_timestamp(*args, **kwargs):
        return None

    # monkeypatch.setattr(IbClient, "request_historical_data", mock_hist_request, raising=True)
    monkeypatch.setattr(HistoricalDataService, "get_latest_timestamp", mock_no_timestamp, raising=True)

    # ib_client = IbClient()
    data_service = HistoricalDataService()
    contract = {'con_id': 8942, 'symbol': 'KSS', 'currency': 'USD', 'exchange': 'amex'}
    hist_runner = HistoricalRunner(historical_data_service= data_service,
                                   start_date='2000-01-01', end_date='2019-10-10')
    contract, params = hist_runner.adjust_params(contract)
    assert params
    assert contract
