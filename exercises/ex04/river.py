"""File to define River class."""

__author__ = "730807114"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """River contains bears and fish."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

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

    def check_ages(self) -> None:
        """Remove the fish older than 3 and bear older than 5."""
        rest_of_fish: list[Fish] = []
        rest_of_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                rest_of_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                rest_of_bears.append(bear)

        self.fish = rest_of_fish
        self.bears = rest_of_bears

    def remove_fish(self, amount: int) -> None:
        """Remove fish from frontmost."""
        remained_fish: list[Fish] = []
        i: int = amount
        while i < len(self.fish):
            remained_fish.append(self.fish[i])
            i += 1
        self.fish = remained_fish

    def bears_eating(self) -> None:
        """For each bear, if at least 5 fish in the river, then eat 3."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self) -> None:
        """Checks hunger score of every bear."""
        healthy_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                healthy_bears.append(bear)
        self.bears = healthy_bears

    def repopulate_fish(self) -> None:
        """Each pair of fish will produce 4 offspring."""
        baby_fish: int = (len(self.fish) // 2) * 4
        i: int = 0
        while i < baby_fish:
            self.fish.append(Fish())
            i += 1

    def repopulate_bears(self) -> None:
        """Each pair of bear will produce 1 offspring."""
        baby_bears: int = len(self.bears) // 2
        i: int = 0
        while i < baby_bears:
            self.bears.append(Bear())
            i += 1

    def view_river(self) -> None:
        """Print out river status."""
        print("~~~ Day " + str(self.day) + ": ~~~")
        print("Fish population:" + str(len(self.fish)))
        print("Bear population:" + str(len(self.bears)))

    def one_river_day(self) -> None:
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
        """Call one_river_day 7 times."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1
