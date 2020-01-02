import tests
from proto.option_params_pb2 import OptionParams


def test_pb():
    pb = OptionParams()
    pb.exchange = 'exchange'
    pb.underlyingConId = 123
    pb.tradingClass = 'td'
    pb.multiplier = 100
    pb.expirations.extend({'213', '234'})
    pb.strikes.extend({1, 2, 4})

    assert {'213', '234'} == set(pb.expirations)
    assert {1, 2, 4} == set(pb.strikes)
