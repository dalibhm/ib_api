from enum import Enum


class DownloadConfigType(Enum):
    Populate_Stock_In_Exchange = 1,
    Download_Stock_Data = 2


download_config_type_map = {'populate stocks in exchange': DownloadConfigType.Populate_Stock_In_Exchange,
                            'data download': DownloadConfigType.Download_Stock_Data
                            }


class DownloadConfig:
    def __init__(self, download_config_type):
        self.type = download_config_type_map[download_config_type]


class PopulateStockExchangeConfig(DownloadConfig):
    def __init__(self, download_config):
        super().__init__(download_config['type'])
        self.exchanges = download_config['config']['exchanges']
        self.instruments = download_config['config']['instruments']


class DownloadStockDataConfig(DownloadConfig):
    def __init__(self, download_config):
        super().__init__(download_config['type'])
        self.stocks = None
        self.exchanges = None
        if 'stocks' in download_config['config']:
            self.stocks = download_config['config']['stocks']
        if 'exchanges' in download_config['config']:
            self.exchanges = download_config['config']['exchanges']
        self.data_config = download_config['config']['data']


class DownloadConfigFactory:
    @staticmethod
    def create(download_config):
        download_config_type = download_config_type_map[download_config['type']]
        if download_config_type == DownloadConfigType.Populate_Stock_In_Exchange:
            return PopulateStockExchangeConfig(download_config)
        elif download_config_type == DownloadConfigType.Download_Stock_Data:
            return DownloadStockDataConfig(download_config)

