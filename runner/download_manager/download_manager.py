from time import sleep

from custom_types.request_type import RequestType
from request_templates.params import RequestTemplate


class DownloadManager:
    def __init__(self, contract, request_template: RequestTemplate, services):
        self.services = services
        self.contract = contract
        self.request_template = request_template

    def run(self):
        # if self.request_template.type == RequestType.Fundamental and not self.check_calendar():
        #     self.send()
        self.send()

    def check_calendar(self):
        self.services['fundamental'].is_up_to_date(self.contract['symbol'])

    def send(self):
        if self.request_template.type == RequestType.Fundamental:
            for report_type in self.request_template.params:
                self.services['ib'].request_fundamental_data(self.contract, report_type)
                sleep(0.5)
        elif self.request_template.type == RequestType.Historical:
            self.services['ib'].request_historical_data(self.contract, self.request_template.params)
        else:
            raise Exception('request object is neither FundamentalRequest nor HistoricalRequest')