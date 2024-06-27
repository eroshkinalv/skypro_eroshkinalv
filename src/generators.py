from typing import List, Generator
# from data.transactions import *


def filter_by_currency(transactions_list: List, currency: str) -> Generator:
    """Выдает по очереди операции, в которых указана заданная валюта"""

    if currency != "руб.":
        filtered_list = (x for x in transactions_list if x["operationAmount"]["currency"]["code"] == currency)

    else:
        filtered_list = (x for x in transactions_list if x["operationAmount"]["currency"]["name"] == currency)

    return filtered_list


# usd_transactions = filter_by_currency(transactions, "руб.")
#
# # for _ in range(2):
# #     print(next(usd_transactions)["id"])


def transaction_descriptions(transactions_list: List) -> Generator:
    """Возвращает описание каждой операции по очереди"""

    return (x["description"] for x in transactions_list)


# descriptions = transaction_descriptions(transactions)
#
# for _ in range(5):
#     print(next(descriptions))


def card_number_generator(start: int, stop: int) -> List[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне"""

    new_numbers = ["0" * (16 - len(str(num))) + str(num) for num in range(start, stop + 1)]

    return [n[:4] + " " + n[4:8] + " " + n[8:12] + " " + n[12:] for n in new_numbers]


# for card_number in card_number_generator(1, 5):
#     print(card_number)
