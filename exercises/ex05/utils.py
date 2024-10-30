"""List Unit Tests"""

___author___: str = "730766272"


def only_evens(input_list: list[int]) -> list[int]:
    """returns only the even numbers from the given list"""
    even_nums: list[int] = []
    for elem in input_list:
        if elem % 2 == 0:
            even_nums.append(elem)
    return even_nums


def sub(num_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """returns all the numbers in the list between the start and end
    index (end index not included)"""
    idx: int = start_idx
    sub_list: list[int] = []
    if len(num_list) == 0 or start_idx >= len(num_list) or end_idx <= 0:
        return sub_list
    else:
        if start_idx < 0:
            idx = 0
        if end_idx > len(num_list):
            end_idx = len(num_list)
        while idx < end_idx:
            sub_list.append(num_list[idx])
            idx += 1
        return sub_list


def add_at_index(given_list: list[int], num: int, idx: int) -> None:
    """Adds the given number to the list at the specified index"""
    if idx < 0 or idx > len(given_list):
        raise IndexError("Index is out of bounds for the input list")
    given_list.append(0)
    for i in range(len(given_list) - 2, idx - 1, -1):
        given_list[i + 1] = given_list[i]
    given_list[idx] = num
