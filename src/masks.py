import logging

logging.basicConfig(filename=r'..\logs\masks.log', encoding='utf-8',
                    filemode='w',
                    format='%(asctime)s, %(filename)s, %(levelname)s: %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def get_mask_card_number(c_num: int) -> str:
    """Возвращает маску номера карты в формате 'XXXX XX** **** XXXX'"""

    card_num = str(c_num)
    masked_num = card_num[0:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]

    logging.info(f'Номер карты {c_num} скрыт.')

    return masked_num


def get_mask_account(a_num: int) -> str:
    """Возвращает маску номера счета в формате '**XXXX'"""

    acc_num = str(a_num)
    masked_acc = "**" + acc_num[-4:]

    logging.info(f'Номер счета {a_num} скрыт.')

    return masked_acc


if __name__ == '__main__':

    print(get_mask_card_number(int(input())))
    print(get_mask_account(int(input())))
