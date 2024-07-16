import json
import os
from typing import Dict

import requests
from dotenv import load_dotenv

load_dotenv(".env")
currency_exchange_api = os.getenv("EXCHANGE_API_KEY")


def get_transaction_amount_in_rub(transaction: Dict) -> float:
    """Принимает трансакцию (в RUB, USD или EUR) и выдает сумму трансакции в рублях.
       Для конвертации используется Exchange Rates Data API"""

    currency_type = transaction['operationAmount']['currency']['code']
    currency_amount = transaction['operationAmount']['amount']

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_type}&amount={currency_amount}"
    response = json.loads(requests.get(url, headers={"apikey": currency_exchange_api}).text)

    amount = float(response["result"])

    return amount


if __name__ == '__main__':

    transactions = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    print(get_transaction_amount_in_rub(transactions))
