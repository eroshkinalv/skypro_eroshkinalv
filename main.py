import re
from typing import Generator

from src.generators import filter_by_currency, search_dict_by_description
from src.processing import filter_by_state, sort_by_date
from src.utils import json_csv_excel_file_to_python
from src.widget import get_data, mask_account_card


def user_input_yes_no() -> str:
    """Возвращает ответ пользователя: да или нет"""

    while True:
        user_input = input().strip().lower()

        if user_input in ['да', 'нет']:
            break

    return user_input


def main() -> Generator:
    """Отвечает за основную логику проекта и связывает функциональности между собой"""

    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

    while True:
        user_file_type = input().strip()

        if user_file_type in ['1', '2', '3']:
            break

        else:
            print('Выберите необходимый пункт меню. Введите: 1, 2 или 3.')

    if user_file_type == '1':
        file_type = r"C:\Users\liudo\PycharmProjects\skypro_eroshkinalv\data\operations.json"
        print('\nДля обработки выбран JSON-файл.')

    elif user_file_type == '2':
        file_type = r"C:\Users\liudo\PycharmProjects\skypro_eroshkinalv\data\transactions.csv"
        print('\nДля обработки выбран CSV-файл.')

    elif user_file_type == '3':
        file_type = r"C:\Users\liudo\PycharmProjects\skypro_eroshkinalv\data\transactions_excel.xlsx"
        print('\nДля обработки выбран XLSX-файл.')

    dict_list = json_csv_excel_file_to_python(file_type)

    print("""\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    while True:
        user_state_input = input()
        transaction_state = user_state_input.strip().upper()

        if transaction_state in ['EXECUTED', 'CANCELED', 'PENDING']:
            break

        else:
            print(f'Статус операции "{user_state_input}" недоступен.\n')
            print("""\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    data_by_state = filter_by_state(dict_list, transaction_state)

    if data_by_state == []:
        print('\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.')

    else:
        print(f'\nОперации отфильтрованы по статусу "{transaction_state}"\n')

        print('\nОтсортировать операции по дате? Да/Нет')

        if user_input_yes_no() == 'да':
            print('\nОтсортировать по возрастанию или по убыванию?')

            while True:
                user_order_input = ' '.join(input().split()).lower()

                if user_order_input in ['по возрастанию', 'по убыванию', 'возрастанию', 'убыванию']:
                    break

            if user_order_input in ['по возрастанию', 'возрастанию']:
                data_by_date = sort_by_date(data_by_state, False)

            elif user_order_input in ['по убыванию', 'убыванию']:
                data_by_date = sort_by_date(data_by_state)

        else:
            data_by_date = data_by_state

        print('\nВыводить только рублевые тразакции? Да/Нет')

        if user_input_yes_no() == 'да':
            currency_filter = list(filter_by_currency(data_by_date, 'RUB'))

        else:
            currency_filter = data_by_date

        print('\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет')

        if user_input_yes_no() == 'да':
            print('\nВведите слово для поиска:')
            user_word_input = input().strip().lower()
            filter_by_description = search_dict_by_description(currency_filter, user_word_input)

        else:
            filter_by_description = currency_filter

        if filter_by_description == []:
            print('\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.')

        else:

            print('\nРаспечатываю итоговый список транзакций...')

            result = len(filter_by_description)

            print(f'\nВсего банковских операций в выборке: {result}')

            for item in filter_by_description:
                tr_date = get_data(item['date'])
                tr_description = item['description']
                account_to = mask_account_card(item['to'])
                if user_file_type == '1':
                    tr_amount = item['operationAmount']['amount']
                    tr_currency = item['operationAmount']['currency']['name']

                else:
                    tr_amount = item['amount']
                    tr_currency = item['currency_code']

                if re.search(r"перевод", tr_description, re.I) is None:
                    search_result = f'\n{tr_date} {tr_description}\n{account_to}\nСумма: {tr_amount} {tr_currency}'

                else:
                    account_from = mask_account_card(item['from'])
                    search_result = (f'\n{tr_date} {tr_description}'
                                     f'\n{account_from} -> {account_to}'
                                     f'\nСумма: {tr_amount} {tr_currency}')

                yield f'\n{search_result}'


if __name__ == '__main__':
    print(*main())
