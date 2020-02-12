from fundamental_data.mongo_data.statement import Statement
from fundamental_data.mongo_data.mongo_init import global_init

global_init()
a = Statement.objects(ticker='A')