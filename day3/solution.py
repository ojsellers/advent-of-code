import re

import numpy as np


def get_input(filename: str) -> list[str]:
    with open(filename, "r+") as f:
        data = f.read()
    return data.splitlines()


def get_part_lookup(schematic: list[str]) -> dict[str, str]:
    return {
        f"{row_i}:{char_i}": []
        for row_i in range(len(schematic))
        for char_i in range(len(schematic[0]))
        if schematic[row_i][char_i] not in ("0123456789.")
    }


def update_part_numbers(row, row_i, num, part_nums):
    indices = {
        f"{i}:{j}"
        for i in (row_i - 1, row_i, row_i + 1)
        for j in range(num.start() - 1, num.end() + 1)
    }
    for index in indices:
        if part_nums.get(index) is not None:
            part_nums[index].append(int(num.group()))
    return part_nums


def get_part_numbers(schematic: list[str], part_nums: dict) -> list[int]:
    for row_i, row in enumerate(schematic):
        for num in re.finditer(r"\d+", row):
            part_nums = update_part_numbers(row, row_i, num, part_nums)
    return part_nums


def sum_part_numbers(schematic: list[str]) -> int:
    part_nums = get_part_lookup(schematic)
    return sum(sum(v) for v in get_part_numbers(schematic, part_nums).values())


def get_gear_lookup(schematic: list[str]) -> dict[str, str]:
    return {
        f"{row_i}:{char_i}": []
        for row_i in range(len(schematic))
        for char_i in range(len(schematic[0]))
        if schematic[row_i][char_i] == "*"
    }


def sum_gear_ratios(schematic: list[str]) -> int:
    gears = get_gear_lookup(schematic)
    return sum(
        np.product(v)
        for v in get_part_numbers(schematic, gears).values()
        if len(v) == 2
    )


if __name__ == "__main__":
    schematic = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617@......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]
    schematic = get_input("input.txt")
    print(sum_part_numbers(schematic))
    print(sum_gear_ratios(schematic))

