import pytest
# from src.generators import filter_by_currency
# from data.transactions import *


def test_filter_by_currency(transactions):

    usd_transactions = (x for x in transactions if x["operationAmount"]["currency"]["code"] == "USD")

    for _ in range(1):
        result = next(usd_transactions)["id"]

        expected_result = 939719570

        assert result == expected_result

    for _ in range(1):
        result = next(usd_transactions)["id"]

        expected_result = 142264268

        assert result == expected_result


def test_transaction_descriptions(transactions):

    descriptions = (x["description"] for x in transactions)

    for _ in range(1):
        result = next(descriptions)

        expected_result = "Перевод организации"

        assert result == expected_result

    for _ in range(1):
        result = next(descriptions)

        expected_result = "Перевод со счета на счет"

        assert result == expected_result

    for _ in range(1):
        result = next(descriptions)

        expected_result = "Перевод со счета на счет"

        assert result == expected_result

    for _ in range(1):
        result = next(descriptions)

        expected_result = "Перевод с карты на карту"

        assert result == expected_result

    for _ in range(1):
        result = next(descriptions)

        expected_result = "Перевод организации"

        assert result == expected_result


def test_card_number_generator():

    new_numbers = ["0" * (16 - len(str(num))) + str(num) for num in range(1, 5 + 1)]

    result = [n[:4] + " " + n[4:8] + " " + n[8:12] + " " + n[12:] for n in new_numbers]

    assert result == ['0000 0000 0000 0001',
                      '0000 0000 0000 0002',
                      '0000 0000 0000 0003',
                      '0000 0000 0000 0004',
                      '0000 0000 0000 0005']
