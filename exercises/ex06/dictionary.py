"""Dictionary Utility Functions"""

___author___: str = "730766272"


def invert(values: dict[str, str]) -> dict[str, str]:
    inverted_dict: dict[str, str] = {}
    for key in values:
        dict_val: str = values[key]
        count: int = 0
        for key2 in values:
            if dict_val == values[key2]:
                count += 1
        if count > 1:
            raise KeyError("Repeated keys. Cannot Invert")
    for key3 in values:
        inverted_dict[values[key3]] = key3
    return inverted_dict


def favorite_color(fav_colors: dict[str, str]) -> str:
    popular: str = ""
    counter: int = 0
    for key in fav_colors:
        curr_count: int = 0
        curr_value = fav_colors[key]
        for key2 in fav_colors:
            if curr_value == fav_colors[key2]:
                curr_count += 1
        if curr_count > counter:
            counter = curr_count
            popular = curr_value
    return popular


def count(items: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    for item in items:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    by_words: dict[str, list[str]] = {}
    for w in words:
        word = w.lower()
        first_letter = word[0]
        if first_letter in by_words:
            by_words[first_letter].append(word)
        else:
            by_words[first_letter] = [word]
    return by_words


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    if day in attendance_log:
        count: int = 0
        for item in attendance_log[day]:
            if item == student:
                count += 1
        if count == 0:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
