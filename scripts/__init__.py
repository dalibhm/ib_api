import os
import sys
from configparser import ConfigParser


sys.path.append('..')

from sql_data.db_factory import DbSessionFactory

config = ConfigParser()
config.read(os.path.join('..', 'settings', 'development.ini'))

DbSessionFactory.global_init(config) # initializes sql database
