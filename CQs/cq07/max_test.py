from CQs.cq07.find_max import find_and_remove_max

"""Unit tests for the find_max function"""
___author___: str = "730766272"


def test_find_and_remove_max_ret_value() -> None:
    """testing whether the function correctly identifies the maxiumum value"""
    input_list: list[int] = [2, 3, 4, 5, 6]
    max: int = find_and_remove_max(input_list)
    assert max == 6


def test_find_and_remove_max_behavior() -> None:
    """testing whether the maximum value is removed from the list"""
    input_list: list[int] = [2, 3, 4, 5, 6]
    find_and_remove_max(input_list)
    assert input_list == [2, 3, 4, 5]


def test_find_and_remove_max_edge_case() -> None:
    """checking whether max correctly returns in an edge case"""
    edge_list: list[int] = []
    edge_test: int = find_and_remove_max(edge_list)
    assert edge_test == -1
