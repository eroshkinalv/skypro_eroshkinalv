from typing import Generator, List


def filter_by_currency(transactions_list: List, currency: str) -> Generator:
    """Выдает по очереди операции, в которых указана заданная валюта"""

    if currency != "руб.":
        filtered_list = list(x for x in transactions_list if x["operationAmount"]["currency"]["code"] == currency)

    else:
        filtered_list = list(x for x in transactions_list if x["operationAmount"]["currency"]["name"] == currency)

    index = 0

    while True:
        yield filtered_list[index]
        index += 1


def transaction_descriptions(transactions_list: List) -> Generator:
    """Возвращает описание каждой операции по очереди"""

    tr_descriptions = list(x["description"] for x in transactions_list)
    index = 0
    while True:
        yield tr_descriptions[index]
        index += 1


def card_number_generator(start: int, stop: int) -> Generator:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне"""

    new_numbers = ["0" * (16 - len(str(num))) + str(num) for num in range(start, stop + 1)]

    for n in new_numbers:
        yield n[:4] + " " + n[4:8] + " " + n[8:12] + " " + n[12:]


# for card_number in card_number_generator(1, 5):
#     print(card_number)
