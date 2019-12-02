import mongoengine


def global_init():
    mongoengine.register_connection(alias='financialDataRepository',
                                    name='financialData',
                                    host='192.168.1.97')
    # username='ib_test',
    # password='ib_test')
