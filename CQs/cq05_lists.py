"""Mutating functions."""

___author___: str = "730766272"


def manual_append(num: int, num_list: list[int]) -> None:
    num_list.append(num)


def double(num_list2: list[int]) -> None:
    idx: int = 0
    while idx < len(num_list2):
        num_list2[idx] = num_list2[idx] * 2
        idx += 1


list1: list[int] = [1, 2, 3]
list2: list[int] = list1
double(list2)
print(list1)
print(list2)
