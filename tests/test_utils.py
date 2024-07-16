import json
import pandas as pd
from unittest.mock import Mock, patch

from src.utils import json_csv_excel_file_to_python


def test_json_csv_excel_file_to_python_empty_list():

    mock_json = Mock(return_value=[])
    json.load = mock_json

    assert json_csv_excel_file_to_python(r'..\data\operations.json') == []


def test_json_csv_excel_file_to_python_not_list(json_file_dict):

    mock_json = Mock(return_value=json_file_dict)

    json.load = mock_json

    assert json_csv_excel_file_to_python(r'..\data\operations.json') == []


@patch('json.load')
def test_json_csv_excel_file_to_python_json(mock_load):

    mock_load.return_value = [{"id": 587085106}]

    assert json_csv_excel_file_to_python(r'..\data\operations.json') == [{"id": 587085106}]
    # mock_load.assert_called_once_with(r"..\data\operations.json, mode='r', encoding='utf-8'")


@patch('csv.DictReader')
def test_json_csv_excel_file_to_python_csv(mock_reader):

    mock_reader.return_value = [{"id": 587085106}]

    assert json_csv_excel_file_to_python(r'..\data\transactions.csv') == [{"id": 587085106}]


@patch('pandas.DataFrame.to_dict')
def test_json_csv_excel_file_to_python_excel(mock_dict):

    mock_dict.return_value = [{"id": 587085106}]

    assert json_csv_excel_file_to_python(r'..\data\transactions_excel.xlsx') == [{"id": 587085106}]
