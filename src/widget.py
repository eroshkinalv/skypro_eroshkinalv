def get_data(date: str) -> str:
    """Преобразует дату в формат DD.MM.YYYY"""

    date_only = date[:10].split("-")
    date_format = ".".join(date_only[::-1])

    return date_format


print(get_data("2018-07-11T02:26:18.671407"))


def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счета"""

    info_split = info.split()

    account_card = {}
    masked_account_card = {}
    card_type = ""

    for k in info_split:

        if k.isalpha() is True:
            card_type += k + " "

        else:
            account_card[card_type] = int(k)

    for k, v in account_card.items():

        if k != "Счет ":
            from src.masks import get_mask_card_number
            masked_account_card[k] = get_mask_card_number(v)

        else:
            from src.masks import get_mask_account
            masked_account_card[k] = get_mask_account(v)

    return card_type + str(masked_account_card.get(card_type))


print(mask_account_card("Visa Platinum 8990922113665229"))
