from typing import Generator, List


def filter_by_currency(transactions_list: List, currency: str) -> Generator:
    """Выдает по очереди операции, в которых указана заданная валюта"""

    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions_list: List) -> Generator:
    """Возвращает описание каждой операции по очереди"""

    for transaction in transactions_list:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне"""

    new_numbers = ["0" * (16 - len(str(num))) + str(num) for num in range(start, stop + 1)]

    for n in new_numbers:
        yield n[:4] + " " + n[4:8] + " " + n[8:12] + " " + n[12:]
