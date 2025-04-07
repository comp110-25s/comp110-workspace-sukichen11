"""Tea Party Exercise"""

__author__: str = "730807114"


def main_planner(guests: int) -> None:
    """Plans for tea party"""
    print("A Cozy Tea Party for " + str(guests) + " people!")
    print("Tea bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """2 tea bags for each person"""
    return 2 * people


def treats(people: int) -> int:
    """1.5 treats for each person"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost of teabags and treats"""
    return 0.50 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
