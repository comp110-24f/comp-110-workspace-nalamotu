def less_than_10(num: int) -> None:
    """Tell us if num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small Number")
    else:
        print("Big Number")
    print("Have a nice day!")


less_than_10(num=7)


def wake_up(alarm: bool) -> str:
    if alarm:
        return "wake up"
    else:
        return "sleep"


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="s"))


def number_info(num: int) -> int:
    if num < 10:
        print("Small Number")
    elif num % 2 == 0:
        print("Even Number")
    else:
        print("Odd number")
    return num


(number_info(num=11))
print(number_info(num=4))
