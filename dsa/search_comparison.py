import time


transactions = []

for i in range(1, 21):

    transactions.append({
        "transaction_id": i,
        "amount": i * 1000
    })


transaction_dict = {
    t["transaction_id"]: t
    for t in transactions
}


def linear_search(transaction_id):

    for transaction in transactions:

        if transaction["transaction_id"] == transaction_id:
            return transaction

    return None


def dictionary_lookup(transaction_id):

    return transaction_dict.get(transaction_id)


target_id = 20


start = time.perf_counter()

linear_result = linear_search(target_id)

linear_time = time.perf_counter() - start


start = time.perf_counter()

dict_result = dictionary_lookup(target_id)

dict_time = time.perf_counter() - start


print("LINEAR SEARCH RESULT")
print(linear_result)
print(f"Time: {linear_time:.10f} seconds")


print("\nDICTIONARY LOOKUP RESULT")
print(dict_result)
print(f"Time: {dict_time:.10f} seconds")