import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount_in_rub

load_dotenv(".env")
currency_exchange_api = os.getenv("EXCHANGE_API_KEY")


@patch('json.loads')
def test_get_transaction_amount_in_rub(mock_loads):

    mock_loads.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {
            "rate": 148.972231,
            "timestamp": 1519328414},
        "query": {
            "amount": 25,
            "from": "RUB",
            "to": "RUB"},
        "result": 31957.58,
        "success": 'true'
    }

    assert get_transaction_amount_in_rub({
        "id": 441945886,
        "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}}) == 31957.58
    # mock_loads.assert_called_once(requests.get('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=RUB&amount=31957.58'))
