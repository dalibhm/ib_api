import pytest

import tests
from proto.contract_details_pb2 import ContractDetails as ProtoContractDetails

# @pytest.mark.skip
def test_pb():
    pb = ProtoContractDetails(**tests.contract_details_sample)

