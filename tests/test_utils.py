import json
from unittest.mock import Mock, patch

from src.utils import json_csv_excel_file_to_python


def test_json_csv_excel_file_to_python_empty_list(json_file_abs_path):

    mock_json = Mock(return_value=[])
    json.load = mock_json

    assert json_csv_excel_file_to_python(json_file_abs_path) == []


def test_json_csv_excel_file_to_python_not_list(json_file_dict, json_file_abs_path):

    mock_json = Mock(return_value=json_file_dict)

    json.load = mock_json

    assert json_csv_excel_file_to_python(json_file_abs_path) == []


@patch('json.load')
def test_json_csv_excel_file_to_python_json(mock_load, json_file_abs_path):

    mock_load.return_value = [{"id": 587085106}]

    assert json_csv_excel_file_to_python(json_file_abs_path) == [{"id": 587085106}]
    # mock_load.assert_called_once_with(json_file_abs_path, mode='r', encoding='utf-8')


@patch('csv.DictReader')
def test_json_csv_excel_file_to_python_csv(mock_reader, csv_file_abs_path):

    mock_reader.return_value = [{"id": 587085106}]

    assert json_csv_excel_file_to_python(csv_file_abs_path) == [{"id": 587085106}]


@patch('pandas.DataFrame.to_dict')
def test_json_csv_excel_file_to_python_excel(mock_dict, xlsx_file_abs_path):

    mock_dict.return_value = [{"id": 587085106}]

    assert json_csv_excel_file_to_python(xlsx_file_abs_path) == [{"id": 587085106}]
