from configparser import ConfigParser

import mongoengine


def global_init(config: ConfigParser):
    mongoengine.register_connection(alias='financialDataRepository',
                                    name=config.get('mongo', 'db'),
                                    host=config.get('mongo', 'host'),
                                    port=config.getint('mongo', 'port')
                                    )
    # username='ib_test',
    # password='ib_test')
