import datetime  # не зря же импорты проходили


def get_data(date: str) -> str:
    """Преобразует дату в формат DD.MM.YYYY"""

    date_only = datetime.datetime(int(date[:4]), int(date[5:7]), int(date[9:10]))
    date_format = date_only.strftime("%d.%m.%y")

    return date_format


# print(get_data("2018-07-11T02:26:18.671407"))


def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счета"""

    info_split = info.split()

    card_type = " ".join([k for k in info_split if k.isalpha() is True])
    card_number = int("".join([k for k in info_split if k.isdigit() is True]))

    if card_type != "Счет":
        from src.masks import get_mask_card_number
        masked_account_card = card_type + " " + get_mask_card_number(card_number)

    else:
        from src.masks import get_mask_account
        masked_account_card = card_type + " " + get_mask_account(card_number)

    return masked_account_card


# print(mask_account_card("Visa Platinum 7000 7922 8960 6361"))
# print(mask_account_card("Maestro 7000 7922 8960 6361"))
# print(mask_account_card("Счет 73654108430135874305"))
