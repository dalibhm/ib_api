from services.ib_client import IbClient
from services.listing_service import ListingService


class Request:
    def __init__(self, contract, request_template):
        self.request_template = request_template
        self.contract = contract

