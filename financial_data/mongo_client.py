import pymongo

conn_string = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn_string)
db = client.xml_test