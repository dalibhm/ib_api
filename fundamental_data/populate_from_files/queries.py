from mongo_data.statement import Statement
from mongo_data.mongo_init import global_init

global_init()
a = Statement.objects(ticker='A')