"""File to define Bear class."""

__author__: str = "730766272"


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor for the bear class intializing attributes."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Increasing age and hunger by one per day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Eating to increase hunger score."""
        self.hunger_score += num_fish
