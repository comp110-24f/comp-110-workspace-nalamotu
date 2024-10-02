"""Functions- Challenge Question 00"""

__author__ = 730766272


def mimic(message: str) -> str:
    """returns the entered string"""
    return message


def main() -> None:
    """Main method with no return type that prints the output of the mimic function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
