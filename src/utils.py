import json
import logging
from typing import Any

logging.basicConfig(filename=r'..\logs\utils.log', encoding='utf-8',
                    filemode='w',
                    format='%(asctime)s, %(filename)s, %(levelname)s: %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def json_file_to_python(json_file: str) -> Any:
    """Принимает JSON-файл и преобразует его объект Python"""

    try:
        with open(json_file, encoding="utf-8") as file:
            data = json.load(file)

            logging.info('JSON-файл успешно преобразован.')

    except (FileNotFoundError, json.JSONDecodeError):
        data = []

        logging.error('Не удается открыть файл: файл не найден/пустой файл.')

        return data

    else:

        if type(data) is not list:
            data = []

            logging.warning('Содержимое JSON-файла не является списком.')

    return data


if __name__ == '__main__':

    print(json_file_to_python(r'..\data\operations.json'))
    print(json_file_to_python('operations.json'))
