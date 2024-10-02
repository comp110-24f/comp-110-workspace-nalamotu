"""A Game like Wordle"""

__author__: str = "730766272"


def input_word() -> str:
    # spacing between strings in print statement important
    five_char_word: str = input("Enter a 5-character word: ")
    if len(five_char_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return five_char_word


def input_letter() -> str:
    single_char: str = input("Enter a single character: ")
    if len(single_char) != 1:
        print("Error: Character must be a single character.")
        exit()
    return single_char


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    # 5 different ifs, cannot use elif as all characters won't be checked
    if letter == word[0]:
        print(letter + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(count, "instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
