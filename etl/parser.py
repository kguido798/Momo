import json


def load_sample_data():
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

    return transactions


if __name__ == "__main__":
    data = load_sample_data()

    print(json.dumps(data, indent=4))