"""Coordinates: Printing every combination of characters of the 2 strings"""

___author___: str = "730766272"


def get_coords(xs: str, ys: str) -> None:
    idx1: int = 0
    idx2: int = 0
    while idx1 < len(xs):
        while idx2 < len(ys):
            print(xs[idx1] + ys[idx2])
            idx2 += 1
        idx2 = 0
        idx1 += 1
