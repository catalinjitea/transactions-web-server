from flask import Flask
from flask import json
from flask import request
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')

mydb = client['web-server-db']

app = Flask(__name__)

@app.route('/transactions', methods = ['GET', 'POST'])
def transactions():
	if request.method == 'GET':
		user = request.args.get('user')
		day = request.args.get('day')
		threshold = request.args.get('threshold')

		cursor = mydb.transactionsTable.find(
			{"$or": [{"sender": user}, {"receiver": user}], 
			"sum": {"$gt": threshold},
			"timestamp": {"$eq": day}})

		for document in cursor:
			print document
		
    	return "OK"

	if request.method == 'POST':
		myrecord = {
			"sender": 1,
			"receiver" : 3,
			"timestamp" : 12345,
			"sum" : 5000
		}
		record_id = mydb.transactionsTable.insert(myrecord)

		print record_id

		return "OK"

@app.route('/balance', methods = ['GET'])
def balance():
	user = request.args.get('user')
	since = request.args.get('since')
	until = request.args.get('until')

	cursor_as_sender = mydb.transactionsTable.find(
		{"sender": user, 
		"timestamp": {"$gte": since},
		"timestamp": {"$lte": until}
		})

	cursor_as_receiver = mydb.transactionsTable.find(
		{"receiver": user, 
		"timestamp": {"$gte": since},
		"timestamp": {"$lte": until}
		})

	balance = 0.0

	print "AS RECEIVER"
	for document in cursor_as_receiver:
		balance += float(document["sum"])
		print document

	print "AS SENDER"
	for document in cursor_as_sender:
		balance -= float(document["sum"])
		print document

	print "BALANCE: ", balance

	return "OK"


if __name__ == '__main__':
	port = 5000 #the custom port you want
	app.run(host='127.0.0.1', port=port)
