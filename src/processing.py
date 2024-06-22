from typing import List, Optional


def filter_by_state(dict_list: List, state: Optional[str] = "EXECUTED") -> List:
    """Возвращает список словарей с заданным ключом(state)"""

    new_dict_list = [k for k in dict_list if k.get("state") == state]

    return new_dict_list


def sort_by_date(dict_list: List, descending_order: Optional[bool] = True) -> List:
    """Сортирует список словарей по доте(date)"""

    if descending_order is False:
        sorted_dict_list = sorted(dict_list, key=lambda d: d["date"])
    else:
        sorted_dict_list = sorted(dict_list, key=lambda d: d["date"], reverse=True)

    return sorted_dict_list
