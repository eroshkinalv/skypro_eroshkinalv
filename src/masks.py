def get_mask_card_number(c_num: int) -> str:
    """Возвращает маску номера в формате 'XXXX XX** **** XXXX'"""

    card_num = str(c_num)
    masked_num = card_num[0:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]

    return masked_num


def get_mask_account(a_num: int) -> str:
    """Возвращает маску счета в формате '**XXXX'"""

    acc_num = str(a_num)
    masked_acc = "**" + acc_num[-4:]

    return masked_acc
