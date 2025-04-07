def count_to_n(n: int) -> None:
    count: int = 0
    while count < n:
        print(f"Count is :{count}")
        count = count + 1


pids: set[int] = {710000000, 712345678}
pids.add(730807114)

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
ice_cream["vanilla"] += 110
