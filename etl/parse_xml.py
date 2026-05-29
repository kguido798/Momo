import xml.etree.ElementTree as ET
import json

XML_FILE = "momo.xml"
JSON_FILE = "../api/data.json"

tree = ET.parse(XML_FILE)
root = tree.getroot()

transactions = []

for transaction in root.findall("transaction"):

    record = {
        "id": int(transaction.find("id").text),
        "type": transaction.find("type").text,
        "amount": int(transaction.find("amount").text),
        "sender": transaction.find("sender").text,
        "receiver": transaction.find("receiver").text,
        "timestamp": transaction.find("timestamp").text
    }

    transactions.append(record)

with open(JSON_FILE, "w") as json_file:
    json.dump(transactions, json_file, indent=4)

print("XML successfully converted to JSON")
