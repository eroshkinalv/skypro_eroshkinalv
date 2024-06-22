import pytest

from src.widget import get_data, mask_account_card


def test_get_data(date_format):
    assert get_data("2018-07-11T02:26:18.671407") == date_format


@pytest.mark.parametrize("number, mask", [
    ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305")]
)
def test_mask_account_card(number, mask):
    assert mask_account_card(number) == mask
