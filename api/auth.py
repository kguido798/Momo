
import base64

USERNAME = "admin"
PASSWORD = "momo123"


def authenticate(headers):
    auth_header = headers.get("Authorization")

    if not auth_header:
        return False

    try:
        auth_type, encoded_credentials = auth_header.split(" ")

        if auth_type != "Basic":
            return False

        decoded_credentials = base64.b64decode(
            encoded_credentials
        ).decode("utf-8")

        username, password = decoded_credentials.split(":")

        return username == USERNAME and password == PASSWORD

    except Exception:
        return False
