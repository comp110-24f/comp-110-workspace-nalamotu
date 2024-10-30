def get_first(input_list: list[str]) -> str:
    """Return first element"""
    return input_list[0]


def remove_first(input_list: list[str]) -> None:
    """Remove first element"""
    input_list.pop(0)


def get_and_remove_first(input_list: list[str]) -> str:
    """Return first element and remove it from input list"""
    first_elem: str = input_list[0]
    input_list.pop(0)
    return first_elem
