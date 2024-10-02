"""While Loops- Challenge Question"""

___author___: str = "730766272"


def num_instances(phrase: str, search_char: str) -> int:
    counter: int = 0  # counts the number of times search_char appears in phrase
    index: int = 0  # index variable for loop counter through phrase
    while index < len(phrase):
        if phrase[index] == search_char:
            counter += 1
        index += 1
    return counter
