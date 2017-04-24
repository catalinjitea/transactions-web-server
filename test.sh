curl -X POST "http://127.0.0.1:5000/transactions?key=listOfUsers"
curl -X GET "http://127.0.0.1:5000/transactions?user=2&day=12345&threshold=2000"
curl -X GET "http://127.0.0.1:5000/balance?user=2&since=12344&until=12345"
