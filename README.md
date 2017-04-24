# Transactions

  I implemented a web server that exposes an API used for adding and analysing transactions performed at a bank. Each transction has a timestamp at which it was performed, the two people involved in the transaction and the amount.
	
### Solution

For this application I used **Flask**, the microframework for Python.
  1. First I imported the Flask class.
  2. Next I create a connection to **MongoDB** using **MongoClient** and I create an instance of the Flask class.
  3. The main logic of the application is in the **transactions** and **balance** methods. I used **route()** decorator to tell Flask what URL should trigger our functions.
    - POST to http://127.0.0.1:5000/transactions/: I created an json object then that contains “sender” - integer, “receiver” - integer, “timestamp” - integer, “sum”.  Then I used **insert()** method to insert the document into a collection named **transactionsTable**.
    - GET to http://127.0.0.1:5000/transactions/?user=XXXX&day=YYYY&threshold=ZZZZ: I used **request.args.get()** to get the parameters value by name  and then I used **find()** to issue a query to retrieve data from a collection in MongoDB.
    - GET to http://127.0.0.1:5000/balance/?user=XXXX&since=YYYY&until=ZZZZ: similar with the previous GET I used find to retrieve the data from the collection. Then to calculate the balance I iterate the cursor for the query where the user was a receiver first, and then when the user was a sender. The balance is the difference between the total amount received minus the total amount sent.
		
To create the Docker image and run the container run:
```
./run.sh
```
 

### Running the tests local

I created some tests to run the application on your machine also. Firstly, you need to install the MongoDB. After that, you need to insert a few transactions into the database.
 ```
 ./insert_some_data.sh
 ```
  
Then start the server and run test.sh which contains 3 tests, one for each operation.
```
python web-server.py
./test.sh
```
