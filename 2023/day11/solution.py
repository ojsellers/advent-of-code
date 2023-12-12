import itertools


def get_input(filename: str):
    with open(filename, "r+") as f:
        data = f.read()
    data = [list(line) for line in data.splitlines() if line]
    return data


def get_empty_rows_cols(space: list[list[str]]) -> (list, list):
    rows = [
        y
        for y in range(len(space))
        if all(space[y][x] == "." for x in range(len(space[0])))
    ]
    cols = [
        x
        for x in range(len(space[0]))
        if all(space[y][x] == "." for y in range(len(space)))
    ]
    return rows, cols


def get_starting_galaxy_coords(
    space: list[list[str]],
) -> dict[int : list[int, int]]:
    galaxies = {}
    number = 1
    for y, x in itertools.product(range(len(space)), range(len(space[0]))):
        if space[y][x] == "#":
            galaxies[number] = [x, y]
            number += 1
    return galaxies


def get_galaxies(
    space: list[list[str]], scale: int
) -> dict[int : list[int, int]]:
    galaxies = get_starting_galaxy_coords(space)
    empty_rows, empty_cols = get_empty_rows_cols(space)
    for number, coords in galaxies.items():
        row_count = sum(row < coords[1] for row in empty_rows)
        col_count = sum(col < coords[0] for col in empty_cols)
        galaxies[number] = [
            coords[0] + col_count * (scale - 1),
            coords[1] + row_count * (scale - 1),
        ]
    return galaxies


def calculate_distance(g1: list[int, int], g2: list[int, int]) -> int:
    return abs(g2[1] - g1[1]) + abs(g2[0] - g1[0])


def get_sum_galaxy_distances(galaxies: dict[int : list[int, int]]) -> int:
    return sum(
        calculate_distance(galaxies[g1], galaxies[g2])
        for g1, g2 in itertools.combinations(galaxies.keys(), 2)
    )


if __name__ == "__main__":
    space = get_input("test_input.txt")
    galaxies = get_galaxies(space, scale=2)
    assert get_sum_galaxy_distances(galaxies) == 374

    space = get_input("input.txt")
    galaxies = get_galaxies(space, scale=2)
    print(get_sum_galaxy_distances(galaxies))

    space = get_input("test_input.txt")
    galaxies = get_galaxies(space, scale=10)
    assert get_sum_galaxy_distances(galaxies) == 1030

    space = get_input("test_input.txt")
    galaxies = get_galaxies(space, scale=100)
    assert get_sum_galaxy_distances(galaxies) == 8410

    space = get_input("input.txt")
    galaxies = get_galaxies(space, scale=1000000)
    print(get_sum_galaxy_distances(galaxies))
