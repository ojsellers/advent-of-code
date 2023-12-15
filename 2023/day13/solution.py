import itertools


def get_input(filename: str):
    with open(filename, "r+") as f:
        data = f.read()
    data = data.split("\n\n")
    return [[list(line) for line in d.splitlines() if line] for d in data]


def check_col(x: int, pattern: list[str], smudges: int) -> bool:
    to_check = x if x < len(pattern[0]) / 2 else len(pattern[0]) - x
    errors = 0
    for row, i in itertools.product(pattern, range(to_check)):
        if row[x - (i + 1)] != row[x + i]:
            errors += 1
            if errors > smudges:
                return False
    return errors >= smudges


def check_row(y: int, pattern: list[str], smudges: int) -> bool:
    to_check = y if y < len(pattern) / 2 else len(pattern) - y
    errors = 0
    for x, i in itertools.product(range(len(pattern[0])), range(to_check)):
        if pattern[y - (i + 1)][x] != pattern[y + i][x]:
            errors += 1
            if errors > smudges:
                return False
    return errors >= smudges


def reflection_lines_sum(
    patterns: list[list[list[str]]], smudges: int = 0
) -> int:
    sum_val = 0
    for pattern in patterns:
        col_is = [
            x
            for x in range(1, len(pattern[0]))
            if check_col(x, pattern, smudges)
        ]
        row_is = [
            y for y in range(1, len(pattern)) if check_row(y, pattern, smudges)
        ]
        sum_val += sum(col_is) + sum(row_is) * 100
    return sum_val


if __name__ == "__main__":
    patterns = get_input("test_input.txt")
    print(reflection_lines_sum(patterns))

    patterns = get_input("input.txt")
    print(reflection_lines_sum(patterns))

    patterns = get_input("test_input.txt")
    print(reflection_lines_sum(patterns, 1))

    patterns = get_input("input.txt")
    print(reflection_lines_sum(patterns, 1))
