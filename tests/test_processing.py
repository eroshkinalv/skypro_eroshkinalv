from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_e(dict_list, dict_list_executed):
    assert filter_by_state(dict_list) == dict_list_executed


def test_filter_by_state_c(dict_list, dict_list_canceled):
    assert filter_by_state(dict_list, "CANCELED") == dict_list_canceled


def test_sort_by_date_d(dict_list, sorted_dict_list_d):
    assert sort_by_date(dict_list) == sorted_dict_list_d


def test_sort_by_date_a(dict_list, sorted_dict_list_a):
    assert sort_by_date(dict_list, False) == sorted_dict_list_a
