from configparser import ConfigParser

import mongoengine


def global_init(config: ConfigParser):
    mongoengine.register_connection(alias='financialDataRepository',
                                    name=config.get('db'),
                                    host=config.get('host'),
                                    port=config.getint('port')
                                    )
    # username='ib_test',
    # password='ib_test')
