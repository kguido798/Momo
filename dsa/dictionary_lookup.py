def build_dictionary(transactions):

    transaction_dict = {}

    for transaction in transactions:

        transaction_dict[
            transaction["id"]
        ] = transaction

    return transaction_dict


def dictionary_lookup(
    transaction_dict,
    target_id
):

    return transaction_dict.get(target_id)
