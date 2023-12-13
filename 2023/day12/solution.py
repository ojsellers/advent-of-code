import functools


def get_input(filename: str):
    with open(filename, "r+") as f:
        data = f.read()
    return [line for line in data.splitlines() if line]


@functools.cache
def calculate_arrangements(condition: str, broken_counts: tuple[int]) -> int:
    if not broken_counts:
        return int(all(c in (".", "?") for c in condition))
    elif len(condition) < sum(broken_counts):
        return 0
    elif condition[0] == ".":
        return calculate_arrangements(condition[1:], broken_counts)

    count = 0
    req_len = broken_counts[0]
    if all(c != "." for c in condition[:req_len]) and (
        len(condition) > req_len
        and condition[req_len] != "#"
        or len(condition) <= req_len
    ):
        count += calculate_arrangements(
            condition[req_len + 1 :], broken_counts[1:]
        )
    if condition[0] == "?":
        count += calculate_arrangements(condition[1:], broken_counts)

    return count


def count_arrangements(conditions: list[str]) -> int:
    count = 0
    for condition in conditions:
        condition = condition.split(" ")
        broken_counts = tuple(int(c) for c in condition[1].split(","))
        count += calculate_arrangements(condition[0], broken_counts)
    return count


def count_arrangements_2(conditions: list[str]) -> int:
    count = 0
    for condition in conditions:
        condition = condition.split(" ")
        broken_counts = tuple(
            int(c) for _ in range(5) for c in condition[1].split(",")
        )
        condition = "?".join([condition[0] for _ in range(5)])
        count += calculate_arrangements(condition, broken_counts)
    return count


if __name__ == "__main__":
    input_txt = get_input("test_input.txt")
    print(count_arrangements(input_txt))

    input_txt = get_input("input.txt")
    print(count_arrangements(input_txt))

    input_txt = get_input("test_input.txt")
    print(count_arrangements_2(input_txt))

    input_txt = get_input("input.txt")
    print(count_arrangements_2(input_txt))
