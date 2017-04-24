from pymongo import MongoClient
import sys
import datetime

client = MongoClient('mongodb://localhost:27017/')

# data base name : 'test-database-1'
mydb = client['web-server-db']

myrecord = {
	"sender": sys.argv[1],
	"receiver": sys.argv[2],
	"timestamp" : sys.argv[3],
	"sum" : sys.argv[4]
}

record_id = mydb.transactionsTable.insert(myrecord)
