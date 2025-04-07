"""File to define Fish class."""

__author__ = "730807114"


class Fish:
    """Fish in river."""

    age: int

    def __init__(self) -> None:
        """New fish."""
        self.age = 0

    def one_day(self) -> None:
        """Increase age by 1."""
        self.age += 1
