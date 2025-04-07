"""File to define Bear class."""

__author__ = "730807114"


class Bear:
    """Bears in river."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """New bear."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Increase age by 1 and decrease hunger score by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Increase hunger score by num_fish."""
        self.hunger_score += num_fish
