"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__: str = "730766272"


class River:
    """River containg bears and fish."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removing old animals."""
        i: int = 0
        j: int = 0
        alive_fish: list[Fish] = []
        alive_bears: list[Bear] = []
        if self.fish != []:
            while i < len(self.fish):
                if self.fish[i].age <= 3:
                    alive_fish.append(self.fish[i])
                i += 1
            self.fish = alive_fish
        if self.bears != []:
            while j < len(self.bears):
                if self.bears[j].age <= 5:
                    alive_bears.append(self.bears[j])
                j += 1
            self.bears = alive_bears

    def bears_eating(self):
        """Bears eating function."""
        for i in range(len(self.bears)):
            if len(self.fish) >= 5:
                River.remove_fish(self, 3)
                self.bears[i].eat(3)

    def check_hunger(self):
        """Removing the bears that starve."""
        alive_bears: list[Bear] = []

        for i in range(len(self.bears)):
            if self.bears[i].hunger_score >= 0:
                alive_bears.append(self.bears[i])
        self.bears = alive_bears

    def repopulate_fish(self):
        """Adding new fish to the river."""
        for i in range((len(self.fish) // 2) * 4):
            baby_fish: Fish = Fish()
            self.fish.append(baby_fish)

    def repopulate_bears(self):
        """Adding new bears to the river."""
        for i in range(len(self.bears) // 2):
            baby_bear: Bear = Bear()
            self.bears.append(baby_bear)

    def view_river(self) -> None:
        """Seeing the day and number of animals in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulating one week in the river."""
        for i in range(7):
            River.one_river_day(self)

    def remove_fish(self, amount: int) -> None:
        """Removing fish from the river."""
        if amount < len(self.fish):
            for i in range(amount):
                self.fish.pop(i)
        else:
            self.fish = []
