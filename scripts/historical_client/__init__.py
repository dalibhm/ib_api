


from configparser import ConfigParser

from mongodb.mongo_setup import global_init
# from program import init_db
from sql_data.db_factory import DbSessionFactory

config = ConfigParser()
config.read('../settings/development.ini')
global_init()
DbSessionFactory.global_init(config)  # initializes sql database