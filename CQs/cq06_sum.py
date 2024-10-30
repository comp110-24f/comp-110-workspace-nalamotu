"""Summing the elements of a list using different loops"""

___author___: str = "730766272"


def w_sum(vals: list[float]) -> float:  # calculating the sum using a while loop
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:  # calculating the sum using a for loop
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    # calculating the sum using a for loop with the range keyword
    sum: float = 0.0
    for idx in range(len(vals)):
        sum += vals[idx]
    return sum
