# import logging
# import os
# import time
#
# from data.db_factory import DbSessionFactory
#
#
# def init_db(config):
#     # settings = config.get_settings()
#     # db_file = settings.get('db_filename')
#
#     DbSessionFactory.global_init()
#
#
# def init_logger():
#     if not os.path.exists("log"):
#         os.makedirs("log")
#
#     log_file = time.strftime("stock_list_%Y%m%d_%H.%M.%S.log")
#     recfmt = '(%(threadName)s) %(asctime)s.%(msecs)03d %(levelname)s %(filename)s:%(lineno)d %(message)s'
#     timefmt = '%y%m%d_%H:%M:%S'
#
#     logger = logging.getLogger('stock_parser')
#     logger.setLevel(logging.INFO)
#     formatter = logging.Formatter(fmt=recfmt, datefmt=timefmt)
#     file_handler = logging.FileHandler(log_file)
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#
#     console = logging.StreamHandler()
#     console.setLevel(logging.ERROR)
#     logger.addHandler(console)
#     return logger
