import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount_in_rub

load_dotenv(".env")
currency_exchange_api = os.getenv("EXCHANGE_API_KEY")


@patch('json.loads')
def test_get_transaction_amount_in_rub(mock_loads, json_file_dict, external_api_return):

    mock_loads.return_value = external_api_return

    assert get_transaction_amount_in_rub(json_file_dict) == 48223.05
    # mock_loads.assert_called_once(requests.get('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=RUB&amount=31957.58'))
