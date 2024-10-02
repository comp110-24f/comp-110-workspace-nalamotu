"""Conditionals- Challenge Question 02"""

___author___: str = "730766272"


def guess_a_number() -> None:
    secret: int = 7
    num = int(input("Guess a number:"))
    print("Your guess was", +num)
    if num == secret:
        print("You got it!")
    elif num < secret:
        print("Your guess was too low! The secret number is", +secret)
    else:
        print("Your guess was too high! The secret number is", +secret)
    return None


if __name__ == "__main__":
    guess_a_number()
