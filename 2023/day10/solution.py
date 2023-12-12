"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.

Direction mapping: x,y where right and down is +ve
"""
import sys

DIRECTIONS = [[1, 0], [0, 1], [-1, 0], [0, -1]]


DIRECTION_MAP = {
    "1,0": {
        "-": [1, 0],
        "J": [0, -1],
        "7": [0, 1],
    },
    "0,1": {
        "|": [0, 1],
        "L": [1, 0],
        "J": [-1, 0],
    },
    "-1,0": {
        "-": [-1, 0],
        "L": [0, -1],
        "F": [0, 1],
    },
    "0,-1": {"|": [0, -1], "7": [-1, 0], "F": [1, 0]},
}


def get_input(filename: str):
    with open(filename, "r+") as f:
        data = f.read()
    data = [list(line) for line in data.splitlines() if line]
    return data


def get_starting_point(tiles: list[list[str]]) -> list:
    return [
        [x, y]
        for y, _tiles in enumerate(tiles)
        for x, tile in enumerate(_tiles)
        if tile == "S"
    ][0]


def _check_valid_point(x: int, y: int, tiles: list[list[str]]) -> bool:
    return x >= 0 and x < len(tiles[0]) and y >= 0 and y < len(tiles)


def get_starting_direction(start: list, tiles: list[list[str]]) -> list:
    for direction in DIRECTIONS:
        x = start[0] + direction[0]
        y = start[1] + direction[1]
        if _check_valid_point(x, y, tiles) and (
            DIRECTION_MAP[f"{direction[0]},{direction[1]}"].get(tiles[y][x])
        ):
            return direction


def check_direction(
    current: list, direction: list, tiles: list[list[str]], distance: int
) -> list[list[str]]:
    x = current[0] + direction[0]
    y = current[1] + direction[1]
    if _check_valid_point(x, y, tiles) and (
        dir := DIRECTION_MAP[f"{direction[0]},{direction[1]}"].get(tiles[y][x])
    ):
        tiles[y][x] = distance
        return check_direction([x, y], dir, tiles, distance + 1)
    return tiles


def apply_transformations(
    start: list, tiles: list[list[str]]
) -> list[list[str]]:
    tiles[start[1]][start[0]] = 0
    start_dir = get_starting_direction(start, tiles)
    return check_direction(start, start_dir, tiles, 1)


def apply_transformations_and_get_max_distance(
    tiles: list[list[str]],
) -> int:
    start = get_starting_point(tiles)
    tiles = apply_transformations(start, tiles)
    # max distance away will be half the total steps from start to start point
    return (
        max(
            n
            for d in DIRECTIONS
            if isinstance((n := tiles[start[1] + d[1]][start[0] + d[0]]), int)
        )
        + 1
    ) // 2


def get_points(start: list, tiles: list[list]) -> list[list]:
    points = {
        tiles[y][x]: [x, y]
        for y in range(len(tiles))
        for x in range(len(tiles[0]))
        if isinstance(tiles[y][x], int)
    }
    max_num = max(
        n
        for d in DIRECTIONS
        if isinstance((n := tiles[start[1] + d[1]][start[0] + d[0]]), int)
    )
    return [
        v[1]
        for v in sorted(
            {k: v for k, v in points.items() if k <= max_num}.items()
        )
    ]


def apply_shoelace_formula(points: list[list]) -> float:
    """From reddit thread"""
    padded_points = [*points, points[0]]
    return (
        sum(
            row1 * col2 - row2 * col1
            for (row1, col1), (row2, col2) in zip(
                padded_points, padded_points[1:]
            )
        )
        / 2
    )


def apply_picks_theorem(area: float, points: list[list]) -> int:
    """From reddit thread"""
    return int(abs(area) - 0.5 * len(points) + 1)


def apply_transformations_and_get_enclosed_tile_count(
    tiles: list[list[str]],
) -> int:
    start = get_starting_point(tiles)
    tiles = apply_transformations(start, tiles)
    points = get_points(start, tiles)
    area = apply_shoelace_formula(points)
    return apply_picks_theorem(area, points)


if __name__ == "__main__":
    # have to increase the recursion limit or it break
    sys.setrecursionlimit(100000)

    tiles = get_input("test_input.txt")
    print(apply_transformations_and_get_max_distance(tiles))

    tiles = get_input("input.txt")
    print(apply_transformations_and_get_max_distance(tiles))

    tiles = get_input("test_input_2.txt")
    print(apply_transformations_and_get_enclosed_tile_count(tiles))

    tiles = get_input("input.txt")
    print(apply_transformations_and_get_enclosed_tile_count(tiles))
