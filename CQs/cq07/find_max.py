"""Finding and removing the largest value in a list"""

___author__: str = "730766272"


def find_and_remove_max(num_list: list[int]) -> int:
    if num_list == []:
        return -1
    else:
        idx: int = 0
        max: int = num_list[idx]
        while idx < len(num_list):  # code to find max
            if num_list[idx] > max:
                max = num_list[idx]
            idx += 1
        idx2: int = 0
        while idx2 < len(num_list):  # code to remove max from the array
            if num_list[idx2] == max:
                num_list.pop(idx2)
            else:
                idx2 += 1
        return max
