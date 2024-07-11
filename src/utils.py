import json
from typing import Any


def json_file_to_python(json_file: str) -> Any:
    """Принимает JSON-файл и преобразует его объект Python"""

    # data = []

    try:
        with open(json_file, encoding="utf-8") as file:
            data = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        data = []
        return data

    else:

        if type(data) is not list:
            data = []

    return data


if __name__ == '__main__':
    print(json_file_to_python(r'..\data\operations.json'))
    print(json_file_to_python('operations.json'))
