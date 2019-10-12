# from configparser import ConfigParser
#
# from Services.LogService import LogService
#
#
# def main(_, **settings):
#     # config = Configurator(settings=settings)
#     config = ConfigParser(settings=settings)
#     config = {
#         'log_level': 'INFO',
#         'log_filename': ''
#     }
#
#     init_logging(config)  # runs first
#
#
# def init_logging(config):
#     settings = config.get_settings()
#     log_level = settings.get('log_level')
#     log_filename = settings.get('log_filename')
#
#     LogService.global_init(log_level, log_filename)
#
#     # log_package_versions()
