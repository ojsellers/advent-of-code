import numpy as np
from tqdm import tqdm


def get_input(filename: str) -> list[str]:
    with open(filename, "r+") as f:
        data = f.read()
    return [line for line in data.splitlines() if line]


def get_num_winning_ways(time: int, record: int) -> int:
    wins = 0
    for i in tqdm(range(time + 1)):
        hold_time = i
        run_time = time - i
        distance = run_time * hold_time
        if distance > record:
            wins += 1
    return wins


def get_total_wins(races: list[str]) -> int:
    times = [int(v) for v in races[0].split(":")[-1].split(" ") if v]
    records = [int(v) for v in races[1].split(":")[-1].split(" ") if v]
    num_wins = [
        get_num_winning_ways(time, record)
        for time, record in zip(times, records)
    ]
    return np.product(num_wins)


def get_total_wins_2(races: list[str]) -> int:
    time = int("".join(v for v in races[0].split(":")[-1].split(" ") if v))
    record = int("".join(v for v in races[1].split(":")[-1].split(" ") if v))
    return get_num_winning_ways(time, record)


if __name__ == "__main__":
    races = get_input("test_input.txt")
    print(get_total_wins(races))

    races = get_input("input.txt")
    print(get_total_wins(races))

    races = get_input("test_input.txt")
    print(get_total_wins_2(races))

    races = get_input("input.txt")
    print(get_total_wins_2(races))

