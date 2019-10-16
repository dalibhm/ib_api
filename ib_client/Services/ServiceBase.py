import logging

# import logbook


class ServiceBase:

    def __init__(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.setLevel(logging.INFO)
        log_name = '{}.log'.format(type(self).__name__.replace("Controller", ""))
        file_handler = logging.FileHandler(log_name)
        formatter = logging.Formatter('%(asctime)-15s %(levelname)s %(name)-s %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # log_name = 'Ctrls/' + type(self).__name__.replace("Controller", "")
        # self.log = logbook.Logger(log_name)
