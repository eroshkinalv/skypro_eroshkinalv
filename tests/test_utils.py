import json
from unittest.mock import Mock, patch

from src.utils import json_file_to_python


def test_json_file_to_python_empty_list():

    mock_json = Mock(return_value=[])
    json.load = mock_json

    assert json_file_to_python(r'..\data\operations.json') == []


def test_json_file_to_python_not_list(json_file_dict):

    mock_json = Mock(return_value=json_file_dict)

    json.load = mock_json

    assert json_file_to_python(r'..\data\operations.json') == []


@patch('json.load')
def test_json_file_to_python_list(mock_load):

    mock_load.return_value = [{"id": 587085106}]

    assert json_file_to_python(r'..\data\operations.json') == [{"id": 587085106}]
