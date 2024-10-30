from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""Unit Tests for the 3 functions"""

___author___: str = "730766272"


def test_only_evens_ret_value() -> None:
    test_list: list[int] = [2, 4, 5, 6, 7, 8, 9, 10]
    output_list: list[int] = only_evens(test_list)
    assert output_list == [2, 4, 6, 8, 10]


def test_only_evens_behavior() -> None:
    test_list: list[int] = [2, 4, 5, 6, 7, 8, 9, 10]
    only_evens(test_list)
    assert test_list == [2, 4, 5, 6, 7, 8, 9, 10]


def test_only_evens_edge_case() -> None:
    edge_test_list: list[int] = []
    output_list = only_evens(edge_test_list)
    assert output_list == []


def test_sub_ret_value() -> None:
    test_list: list[int] = [45, 50, 55, 60, 65, 70]
    output_list: list[int] = sub(test_list, 1, 5)

    test_list_2: list[int] = [45, 50, 55, 60, 65, 70]
    output_list_3: list[int] = sub(test_list_2, -1, 3)
    assert output_list == [50, 55, 60, 65]
    assert output_list_3 == [45, 50, 55]


def test_sub_behavior() -> None:
    test_list: list[int] = [45, 50, 55, 60, 65, 70]
    sub(test_list, 1, 5)
    assert test_list == [45, 50, 55, 60, 65, 70]


def test_sub_edge_case() -> None:
    edge_test_list: list[int] = []
    output_list = sub(edge_test_list, 1, 5)
    assert output_list == []


def test_add_at_index_ret_value() -> None:
    test_list: list[int] = [5, 6, 7, 8, 9, 10]
    add_at_index(test_list, 15, 2)
    assert add_at_index(test_list, 15, 2) is None


def test_add_at_index_behavior() -> None:
    test_list: list[int] = [5, 6, 7, 8, 9, 10]
    add_at_index(test_list, 15, 2)
    assert test_list == [5, 6, 15, 7, 8, 9, 10]


def test_add_at_index_edge_case() -> None:
    edge_test_list: list[int] = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(edge_test_list, 3, 8)
