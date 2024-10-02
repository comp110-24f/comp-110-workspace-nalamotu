"""A Program to play Wordle"""

__author__: str = "730766272"


def input_guess(secret_word_len: int) -> str:
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """checking if the word guess contains a particular character"""
    assert len(char_guess) == 1
    index: int = 0
    count: int = 0
    check: bool = False
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            count += 1  # keeps track of the occurunces of the character in the particular word, 0 means it never occurs
            check = True
        index += 1
        if count == 0:
            check = False
    return check


def emojified(guess: str, secret: str) -> str:
    """converts the guess into a string of emojis denoting how accurate the
    guess is relative to the secret word"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    output: str = ""
    index: int = 0
    while index < len(guess):
        if contains_char(secret, guess[index]):
            if secret[index] == guess[index]:
                output = (
                    output + f"{GREEN_BOX}"
                )  # need to add a space between the boxes, cant use += operator
            else:
                output = output + f"{YELLOW_BOX}"
        else:
            output = output + f"{WHITE_BOX}"
        index += 1
    return output


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop"""
    count: int = 1
    user_guess: str
    correct_guess: str = ("\U0001F7E9") * len(secret)
    checker: bool = False
    while count <= 6 and checker != True:
        print(f"=== Turn {count}/6 ===")
        user_guess = input_guess(len(secret))
        print(emojified(user_guess, secret))
        if (
            emojified(user_guess, secret) == correct_guess
        ):  # checks whether the guess is correct
            print(f"You won in {count}/6 turns!")
            checker = True  # setting true breaks the while loop
        count += 1
    if checker == False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
