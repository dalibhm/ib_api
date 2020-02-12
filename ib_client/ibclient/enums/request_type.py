from enum import Enum


class RequestType(Enum):
    Historical = 'Historical'
    Fundamental = 'Fundamental'
    ContractDetails = 'ContractDetails'
    SecDefOptParams = 'SecDefOptParams'
