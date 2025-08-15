import re
from collections import Counter
from typing import Dict, Generator, List


def filter_by_currency(transactions_list: List, currency: str) -> Generator:
    """Возвращает по очереди операции, в которых указана заданная валюта"""

    for transaction in transactions_list:

        try:
            transaction["operationAmount"]["currency"]["code"] == currency

        except KeyError:
            if transaction["currency_code"] == currency:
                yield transaction

        else:
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


def search_dict_by_description(dict_list: List, request: str) -> List:
    """Возвращает список словарей, у которых в описании есть заданная для поиска строка.
        dict_list - список словарей с банковскими операциями, request - строка для поиска (*строчными буквами)"""

    search_request = ' '.join(w for w in request.split())
    dict_search = []

    for ds in dict_list:
        description = ds["description"]
        if re.search(rf"{search_request}", description, re.I) is not None:
            dict_search.append(ds)

    if dict_search == []:
        search_request = '|'.join(w for w in request.split() if w not in ['перевод', 'с', 'co', 'на'])
        for ds in dict_list:
            description = ds["description"]
            if re.search(rf"{search_request}", description, re.I) is not None:
                dict_search.append(ds)

    if dict_search == []:
        search_request = ' '.join([w[:-1] for w in request.split()])
        for ds in dict_list:
            description = ds["description"]
            if re.search(rf"{search_request}", description, re.I) is not None:
                dict_search.append(ds)

    return dict_search


def get_transactions_category_dict(dict_list: List, category: List) -> Dict:
    """Считает количество операций в каждой категории.
    возвращает словарь (названия категорий: количество операций в каждой категории);
    dict_list - список словарей с данными банковских операций; category - описание банковской операции"""

    transactions_info = dict(Counter([ds["description"] for ds in dict_list if ds["description"] in category]))

    return transactions_info
