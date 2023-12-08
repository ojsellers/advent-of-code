import math


def get_input(filename: str):
    with open(filename, "r+") as f:
        data = f.read()
    data = [line for line in data.splitlines() if line]
    directions = data[0]
    mapping = {
        _m[0]: _m[1].strip("()").split(", ")
        for m in data[1:]
        if (_m := m.split(" = "))
    }
    return directions, mapping


def _update_current_location(
    directions: str, mapping: dict, current_loc: str, count: int
) -> str:
    direction = directions[
        count - len(directions) * (count // len(directions))
    ]
    return (
        mapping[current_loc][0]
        if direction == "L"
        else mapping[current_loc][1]
    )


def count_steps(directions: str, mapping: dict) -> int:
    count = 0
    current_loc = "AAA"
    while True:
        current_loc = _update_current_location(
            directions, mapping, current_loc, count
        )
        count += 1
        if current_loc == "ZZZ":
            return count


def count_steps_2(directions: str, mapping: dict) -> int:
    counts = []
    current_locs = [k for k in mapping if k[2] == "A"]
    for current_loc in current_locs:
        count = 0
        while True:
            current_loc = _update_current_location(
                directions, mapping, current_loc, count
            )
            count += 1
            if current_loc[2] == "Z":
                counts.append(count)
                break
    return math.lcm(*counts)


if __name__ == "__main__":
    directions, mapping = get_input("test_input.txt")
    print(count_steps(directions, mapping))

    directions, mapping = get_input("input.txt")
    print(count_steps(directions, mapping))

    directions, mapping = get_input("test_input_2.txt")
    print(count_steps_2(directions, mapping))

    directions, mapping = get_input("input.txt")
    print(count_steps_2(directions, mapping))
