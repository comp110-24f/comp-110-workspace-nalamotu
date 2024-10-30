"""List Utility Functions."""

___author___: str = "730766272"


def all(num_list: list[int], num: int) -> bool:
    """Checks if all the integers in the list are equal to a particular integer."""
    idx: int = 0
    count: int = 0
    if len(num_list) == 0:
        return False
    else:
        while idx < len(num_list):
            if num_list[idx] == num:
                count += 1
            idx += 1
        if count == len(
            num_list
        ):  # if count and length of the list are the same, all numbers in the list are equal to the given integer
            return True
        else:
            return False


def max(input: list[int]) -> int:
    """Finds the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    biggest_num: int = input[0]
    while idx < len(input):
        if input[idx] > biggest_num:
            biggest_num = input[idx]
        idx += 1
    return biggest_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if the values in the 2 lists are equal."""
    idx: int = 0
    count: int = 0
    if len(list1) != len(list2):  # checking if the 2 lists are the same length
        return False
    else:
        while idx < len(list1):
            if list1[idx] == list2[idx]:
                count += 1
            idx += 1
        if count == len(list1):
            return True
        else:
            return False


def extend(list1: list[int], list2: list[int]) -> None:
    """Appends the second list to the first."""
    idx: int = 0
    while idx < len(list2):
        list1.append(list2[idx])
        idx += 1
