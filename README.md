MoMo SMS App


Team Name
Dev Note

Team Members

Rene Guido Kayigamba
Elijah Kabatsi
NYIRIHIRWE Yves

Project Description

XML-based SMS transaction records can be parsed, managed, secured, and analyzed using the MoMo SMS App, a Mobile Money SMS transaction processing system. The program exposes the data over a secure REST API after processing transaction messages from a structured XML dataset. 
The project illustrates the principles of API development, CRUD operations, XML parsing, JSON serialization, authentication and security concepts, and the integration of Data Structures & Algorithms (DSA) for effective transaction lookup and management. 
Additionally, the system enables frontend dashboard interface for future reporting and visualization, as well as analytics-ready transaction data storage. 

Project Objectives

The project was developed to:
    Parse XML transaction data into structured JSON objects
    Build secure REST API CRUD endpoints
    Implement Basic Authentication security
    Compare DSA search methods for transaction retrieval
    Document API usage for developers
    Demonstrate backend data management principles
    Provide efficient transaction processing and lookup

System Features

The system is capable of:
    Parsing XML transaction messages
    Cleaning and normalizing transaction data
    Categorizing transaction types
    Converting XML records into JSON objects
    Performing CRUD operations through REST API endpoints
    Protecting endpoints using Basic Authentication
    Returning proper HTTP status codes and responses
    Comparing Linear Search and Dictionary Lookup efficiency
    Storing transaction data in SQLite
    Generating analytics-ready datasets
    Supporting frontend dashboard integration

Technologies Used

Python
SQLite
FastAPI
HTML
CSS
JavaScript
http.server
JSON
XML Parsing Libraries

System Architecture

Architecture Diagram

https://miro.com/app/board/uXjVHV5oNv4=/?share_link_id=722346128313

Project Management

Scrum Board

https://trello.com/b/UpaAck4A/momo-progress

Team Participation Sheet

https://docs.google.com/spreadsheets/d/1C5Ryk1UKJ2mrx45E_IS4nODPmCyxKT1EegwZ7vlHZ3o/edit?usp=sharing

Setup Instructions

Clone the Repository
git clone https://github.com/kguido798/Momo
cd Momo

Install Dependencies
pip install -r requirements.txt

Run XML Parsing
python etl/run.py

Start the API Server
python api/server.py

Data Parsing

XML-formatted Mobile Money SMS transaction records are processed by the system. Transaction data is retrieved, cleaned, normalized, and transformed into structured JSON objects for additional processing and storage using Python XML parsing modules. 
Each transaction record contains important fields such as:
    Transaction ID
    Transaction Type
    Amount
    Sender ID
    Receiver ID
    Timestamp
The parsed data is then used for:
    REST API operations
    Database storage
    Transaction analytics
    DSA search comparisons
    Frontend dashboard integration
    
Example JSON Output

[
    {
        "id": "1",
        "transaction_type": "Transfer",
        "amount": "5000",
        "sender": "Alice",
        "receiver": "Bob",
        "timestamp": "2026-05-20T10:30:00"
    }
]

The parsed JSON objects are stored in the database and made accessible through basic security REST API endpoints.

REST API Implementation

The system implements CRUD operations using Python's http.server.

API Endpoints
Endpoint
Method
Description
/transactions
GET
Retrieve all transactions
/transactions/{id}
GET
Retrieve a single transaction
/transactions
POST
Create a new transaction
/transactions/{id}
PUT
Update an existing transaction
/transactions/{id}
DELETE
Delete a transaction


Authentication & Security

The API is protected using Basic Authentication.

Valid Authentication 
Example

curl -u admin:momo123 http://localhost:8000/transactions


Unauthorized Request 
Example

curl -u wrong:wrong http://localhost:8000/transactions

Unauthorized Response

{
  "error": "Unauthorized"
}

HTTP Status Codes

Code
Meaning
200
Success
201
Resource Created
400
Bad Request
401
Unauthorized
404
Not Found
500
Internal Server Error


Reflection on Basic Authentication

Although basic authentication is easy to use, it has a number of security flaws.
    No encryption
    Username and password are sent with every request
    Vulnerable to interception without HTTPS
    No token expiration present at all

Stronger Alternatives

JWT (JSON Web Tokens)

JWT provides token-based authentication where users log in once and receive a secure token for future requests.

OAuth2

OAuth2 enables secure delegated access and is commonly used for third-party authentication systems such as Google or GitHub login.
These methods are more secure, scalable, and suitable for modern production APIs.

API Documentation

GET /transactions

Request

curl -u admin:momo123 http://localhost:8000/transactions

Response

[
  {
    "id": 1,
    "transaction_type": "Deposit",
    "amount": 10000
  }
]

GET /transactions/{id}

Request

curl -u admin:momo123 http://localhost:8000/transactions/1

Response
{
  "id": 1,
  "transaction_type": "Deposit",
  "amount": 10000
}

POST /transactions

Request

curl -X POST -u admin:momo123 ^
-H "Content-Type: application/json" ^
-d "{\"transaction_type\":\"Transfer\",\"amount\":5000}" ^
http://localhost:8000/transactions

Response

{
  "message": "Transaction added successfully"
}

PUT /transactions/{id}

Request

curl -X PUT -u admin:momo123 ^
-H "Content-Type: application/json" ^
-d "{\"amount\":7000}" ^
http://localhost:8000/transactions/1

Response

{
  "message": "Transaction updated successfully"
}

DELETE /transactions/{id}

Request

curl -X DELETE -u admin:momo123 ^
http://localhost:8000/transactions/1

Response

{
  "message": "Transaction deleted successfully"
}

DSA Integration

The project integrates Data Structures & Algorithms to compare transaction search efficiency.

Linear Search

Linear Search scans transaction records one by one until a matching ID is found.

Advantages
    Simple implementation
    Works on unsorted lists

Disadvantages

    Slow for large datasets
    Time Complexity: O(n)

Dictionary Lookup

Transactions are also stored in a Python dictionary:
transactions_dict = {
    1: {...},
    2: {...}
}

Dictionary lookup retrieves records directly using keys.

Advantages

Extremely fast lookup
Efficient for large datasets
Time Complexity: O(1)

Disadvantages

Slightly higher memory usage

DSA Efficiency Comparison

The system tested both methods using more than 20 transaction records.

Method
Time Complexity
Performance
Linear Search
O(n)
Slower
Dictionary Lookup
O(1)
Faster

Reflection

Dictionary lookup is quicker. It doesn't require scanning the complete list because it makes use of hash tables that directly link keys to values.

Testing & Validation

The API was tested using:
*curl

Test Cases Included

    Successful GET request with authentication
    Unauthorized request with wrong credentials
    Successful POST request
    Successful PUT request
    Successful DELETE request
    
Screenshots of all test cases are included in the screenshots/ folder.
