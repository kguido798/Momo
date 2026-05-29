API Documentation
 Base URL

http://localhost:8000
You get it upon running: python server.py in Momo repository



Authentication

All endpoints require Basic Authentication.

Username:admin
Password:devnote


*GET /transactions

It returns all transactions.
It is achieved upon running the code below in the terminal

curl -u admin:password123 http://localhost:8000/transactions


Response

[
    {
        "id": 1,
        "type": "Deposit",
        "amount": 5000
    }
]


The status codes are

200 meaning Success 
401 meaning Unauthorized 
404 meaning Not Found 

 GET /transactions/{id}
This is to get specific transactions
It is achieved upon running the code below in the terminal

curl -u admin:password123 http://localhost:8000/transactions/1


POST /transactions
It is achieved upon running the code below in the terminal

curl -X POST ^
-u admin:password123 ^
-H "Content-Type: application/json" ^
-d "{\"id\":3,\"type\":\"Transfer\",\"amount\":4000}" ^
http://localhost:8000/transactions


Success Code: 201 Created

PUT /transactions/{id}
It is achieved upon running the code below in the terminal


curl -X PUT ^
-u admin:password123 ^
-H "Content-Type: application/json" ^
-d "{\"amount\":9000}" ^
http://localhost:8000/transactions/1


DELETE /transactions/{id}
It is achieved upon running the code below in the terminal

curl -X DELETE ^
-u admin:password123 ^
http://localhost:8000/transactions/1

