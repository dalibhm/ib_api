from enums.request_type import RequestType
from requestmanager.request.contractdetailsrequest import ContractDetailsRequest
from requestmanager.request.fundamentalrequest import FundamentalRequest
from requestmanager.request.historicalrequest import HistoricalRequest
from requestmanager.request.security_definition_option import SecDefOptParamsRequest

request_constructor_map = {
    RequestType.Historical: HistoricalRequest,
    RequestType.Fundamental: FundamentalRequest,
    RequestType.ContractDetails: ContractDetailsRequest,
    RequestType.SecDefOptParams: SecDefOptParamsRequest
}