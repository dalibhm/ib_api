import mongoengine


def global_init():
    mongoengine.register_connection(alias='financialDataRepository',
                                    name='in_test',
                                    host='localhost')
                                    # username='ib_test',
                                    # password='ib_test')