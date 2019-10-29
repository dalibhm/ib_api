from request_templates.params import HistoricalRequestTemplate, FundamentalRequestTemplate


class RequestTemplateFactory:
    def __init__(self):
        pass

    def create(self, data_config):

        if data_config['type'] == 'historical':
            return HistoricalRequestTemplate(data_config['params'])
        elif data_config['type'] == 'fundamental':
            return FundamentalRequestTemplate(data_config['params'])