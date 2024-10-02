"""Basic syntax of lists"""

my_numbers: list[float] = list()  # constructor
my_numbers: list[float] = []  # literal

# adding an item to the list
my_numbers.append(1.5)
my_numbers.append(2.3)
print(my_numbers)

# creating an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# indexing/subscription notation
last_game: int = game_points[2]
# print(game_points[2])
# print(last_game)

# modifying by index (lists are mutable)
game_points[1] = 72
print(game_points)

# finding length of a list
print(len(game_points))

# removing an item from list
game_points.pop(1)
print(game_points)


def display(num_list: list[int]) -> None:
    index: int = 0
    while index < len(num_list):
        print(num_list[index])
        index += 1


display(game_points)

game_points.append(94)
print(game_points)
