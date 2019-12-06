import mongoengine


def global_init():
    mongoengine.register_connection(alias='financialDataRepository',
                                    name='dev',
                                    host='127.0.0.1')
    # username='ib_test',
    # password='ib_test')
