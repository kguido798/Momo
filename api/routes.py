from utils import load_data, save_data


def get_all_transactions():
    return load_data()


def get_transaction_by_id(transaction_id):
    transactions = load_data()

    for transaction in transactions:
        if str(transaction["id"]) == str(transaction_id):
            return transaction

    return None


def create_transaction(new_transaction):
    transactions = load_data()

    transactions.append(new_transaction)

    save_data(transactions)

    return new_transaction


def update_transaction(transaction_id, updated_data):
    transactions = load_data()

    for index, transaction in enumerate(transactions):

        if str(transaction["id"]) == str(transaction_id):

            transactions[index].update(updated_data)

            save_data(transactions)

            return transactions[index]

    return None


def delete_transaction(transaction_id):
    transactions = load_data()

    for transaction in transactions:

        if str(transaction["id"]) == str(transaction_id):

            transactions.remove(transaction)

            save_data(transactions)

            return True

    return False
