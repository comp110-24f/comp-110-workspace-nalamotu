"""Planning a Tea Party"""

__author__: str = "730766272"


def main_planner(guests: int) -> None:
    """Plan the whole tea party from this function, entrypoint to the program"""
    # Concatenation only works when all the data types are strings, so convert int
    # values also into strings
    print("A Cozy Tea Party for " + str(guests) + " People")
    # Get number of teabags, treats and total cost using the functions created below
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: " + "$" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Calculating the number of teabags needed per person"""
    return people * 2
    # when calling functions in trailhead REPL, remember to call with the function name ex- tea_bags(5) and not just 5


def treats(people: int) -> int:
    """Calculating the number of treats needed based on the number of teas guests are
    expected to drink"""
    # use round function to change float into the nearest integer
    return round(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost of the teas and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
