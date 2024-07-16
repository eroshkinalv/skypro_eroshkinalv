import json
import csv
import pandas as pd
import logging
from typing import Any

logging.basicConfig(filename=r'..\logs\utils.log', encoding='utf-8',
                    filemode='w',
                    format='%(asctime)s, %(filename)s, %(levelname)s: %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def json_csv_excel_file_to_python(file_name: str) -> Any:
    """Принимает JSON-, CSV- или XLSX-файл и преобразует его объект Python"""

    try:
        if file_name.endswith('.json'):
            with open(file_name, mode='r', encoding='utf-8') as file:
                data = json.load(file)

                logging.info('JSON-файл успешно преобразован.')

        elif file_name.endswith('.csv'):
            with open(file_name, mode='r', encoding='utf-8') as file:
                data = list(csv.DictReader(file, delimiter=';'))

                logging.info('CSV-файл успешно преобразован.')

        elif file_name.endswith('.xlsx'):
            data = pd.read_excel(file_name).to_dict(orient='records')

            logging.info('EXCEL-файл успешно преобразован.')

    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        data = []

        logging.error('Не удается открыть файл: файл не найден/пустой файл.')

        return data

    else:

        if type(data) is not list:
            data = []

            logging.warning('Содержимое файла не является списком.')

    return data


if __name__ == '__main__':

    # print(json_csv_excel_file_to_python(r'..\data\transactions.csv'))
    print(json_csv_excel_file_to_python(r'..\data\transactions_excel.xlsx'))
    # print(json_csv_excel_file_to_python(r'..\data\operations.json'))
    # print(json_csv_excel_file_to_python('transactions.csv'))
    # print(json_csv_excel_file_to_python('transactions_excel.xlsx'))
    # print(json_csv_excel_file_to_python('operations.json'))
