"""File to define Fish class."""

__author__: str = "730766272"


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Constructor for fish class intializing attributes."""
        self.age: int = 0

    def one_day(self):
        """Increasing age by 1 per day."""
        self.age += 1
