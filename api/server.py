from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64


USERNAME = "admin"
PASSWORD = "momo123"


transactions = [
    {
        "transaction_id": 1,
        "amount": 5000,
        "sender": "Guido",
        "receiver": "Elijah",
        "transaction_type": "Transfer",
        "timestamp": "2026-05-20 10:30:00"
    },
    {
        "transaction_id": 2,
        "amount": 12000,
        "sender": "Mike",
        "receiver": "Sarah",
        "transaction_type": "Payment",
        "timestamp": "2026-05-20 11:00:00"
    }
]


class MyServer(BaseHTTPRequestHandler):

    def authenticate(self):

        auth_header = self.headers.get("Authorization")

        if auth_header is None:
            return False

        auth_type, credentials = auth_header.split()

        if auth_type != "Basic":
            return False

        decoded = base64.b64decode(
            credentials
        ).decode()

        username, password = decoded.split(":")

        return (
            username == USERNAME
            and password == PASSWORD
        )

    def unauthorized(self):

        self.send_response(401)

        self.send_header(
            "WWW-Authenticate",
            'Basic realm="MoMo API"'
        )

        self.end_headers()

        self.wfile.write(
            b"Unauthorized"
        )

    def do_GET(self):

        if not self.authenticate():
            self.unauthorized()
            return

        # GET all transactions
        if self.path == "/transactions":

            self.send_response(200)

            self.send_header(
                "Content-type",
                "application/json"
            )

            self.end_headers()

            self.wfile.write(
                json.dumps(transactions).encode()
            )

        # GET transaction by ID
        elif self.path.startswith("/transactions/"):

            try:

                transaction_id = int(
                    self.path.split("/")[-1]
                )

                transaction = next(
                    (
                        t for t in transactions
                        if t["transaction_id"] == transaction_id
                    ),
                    None
                )

                if transaction:

                    self.send_response(200)

                    self.send_header(
                        "Content-type",
                        "application/json"
                    )

                    self.end_headers()

                    self.wfile.write(
                        json.dumps(transaction).encode()
                    )

                else:

                    self.send_response(404)
                    self.end_headers()

                    self.wfile.write(
                        b"Transaction not found"
                    )

            except ValueError:

                self.send_response(400)
                self.end_headers()

                self.wfile.write(
                    b"Invalid transaction ID"
                )

        else:

            self.send_response(404)
            self.end_headers()

    def do_POST(self):

        if not self.authenticate():
            self.unauthorized()
            return

        if self.path == "/transactions":

            content_length = int(
                self.headers["Content-Length"]
            )

            post_data = self.rfile.read(
                content_length
            )

            new_transaction = json.loads(
                post_data.decode()
            )

            transactions.append(new_transaction)

            self.send_response(201)

            self.send_header(
                "Content-type",
                "application/json"
            )

            self.end_headers()

            response = {
                "message": "Transaction added successfully",
                "transaction": new_transaction
            }

            self.wfile.write(
                json.dumps(response).encode()
            )

        else:

            self.send_response(404)
            self.end_headers()

    def do_PUT(self):

        if not self.authenticate():
            self.unauthorized()
            return

        if self.path.startswith("/transactions/"):

            try:

                transaction_id = int(
                    self.path.split("/")[-1]
                )

                content_length = int(
                    self.headers["Content-Length"]
                )

                put_data = self.rfile.read(
                    content_length
                )

                updated_data = json.loads(
                    put_data.decode()
                )

                transaction = next(
                    (
                        t for t in transactions
                        if t["transaction_id"] == transaction_id
                    ),
                    None
                )

                if transaction:

                    transaction.update(updated_data)

                    self.send_response(200)

                    self.send_header(
                        "Content-type",
                        "application/json"
                    )

                    self.end_headers()

                    response = {
                        "message": "Transaction updated",
                        "transaction": transaction
                    }

                    self.wfile.write(
                        json.dumps(response).encode()
                    )

                else:

                    self.send_response(404)
                    self.end_headers()

                    self.wfile.write(
                        b"Transaction not found"
                    )

            except ValueError:

                self.send_response(400)
                self.end_headers()

                self.wfile.write(
                    b"Invalid transaction ID"
                )

        else:

            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):

        if not self.authenticate():
            self.unauthorized()
            return

        if self.path.startswith("/transactions/"):

            try:

                transaction_id = int(
                    self.path.split("/")[-1]
                )

                transaction = next(
                    (
                        t for t in transactions
                        if t["transaction_id"] == transaction_id
                    ),
                    None
                )

                if transaction:

                    transactions.remove(transaction)

                    self.send_response(200)

                    self.send_header(
                        "Content-type",
                        "application/json"
                    )

                    self.end_headers()

                    response = {
                        "message": "Transaction deleted"
                    }

                    self.wfile.write(
                        json.dumps(response).encode()
                    )

                else:

                    self.send_response(404)
                    self.end_headers()

                    self.wfile.write(
                        b"Transaction not found"
                    )

            except ValueError:

                self.send_response(400)
                self.end_headers()

                self.wfile.write(
                    b"Invalid transaction ID"
                )

        else:

            self.send_response(404)
            self.end_headers()


host = "localhost"
port = 8000

server = HTTPServer((host, port), MyServer)

print(f"Server running on http://{host}:{port}")

server.serve_forever()