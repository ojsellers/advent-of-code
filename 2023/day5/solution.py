import time


def get_input(filename: str) -> list[str]:
    with open(filename, "r+") as f:
        data = f.read()
    return [line for line in data.splitlines() if line]


def build_mapping_dict(almanac: list[str]) -> dict:
    seed_mapping, i = {}, 0
    for row in almanac:
        if "map" in row:
            i += 1
        else:
            lookup = [int(v) for v in row.split(" ")]
            lower = lookup[1]
            upper = lower + lookup[2] - 1
            trans = lookup[0] - lower
            seed_mapping.setdefault(i, []).append([lower, upper, trans])
    return seed_mapping


def _check_current_conversion(lookup: list, seed: int) -> int:
    for conversion in lookup:
        if (seed >= conversion[0]) and (seed <= conversion[1]):
            seed += conversion[2]
            return seed


def get_smallest_location_number(seeds: list[int], seed_mapping: dict) -> int:
    loc_nums = []
    for seed in seeds:
        for lookup in seed_mapping.values():
            if new_seed := _check_current_conversion(lookup, seed):
                seed = new_seed
        loc_nums.append(seed)
    return min(loc_nums)


def get_seed_numbers_part_2(seeds: list[int]) -> list[int]:
    new_seeds = []
    for i in range(len(seeds) // 2):
        lower = seeds[i * 2]
        upper = lower + seeds[i * 2 + 1] - 1
        new_seeds.append([lower, upper])
    return new_seeds


def apply_conversions(
    nums: list[list[int, int]], lookup: list[list[int, int, int]]
) -> list[list[int, int]]:
    updated_nums = []
    for conv in lookup:
        check_nums = []

        for num in nums:
            # if both numbers are within conversion range
            if (conv[0] <= num[0]) and (num[1] <= conv[1]):
                updated_nums.append([num[0] + conv[2], num[1] + conv[2]])

            # if upper bound is within conversion range
            elif (num[0] < conv[0]) and (conv[0] <= num[1] <= conv[1]):
                updated_nums.append([conv[0] + conv[2], num[1] + conv[2]])
                check_nums.append([num[0], conv[0] - 1])

            # if lower bound is within conversion range
            elif (conv[0] <= num[0] < conv[1]) and (num[1] > conv[1]):
                updated_nums.append([num[0] + conv[2], conv[1] + conv[2]])
                check_nums.append([conv[1] + 1, num[1]])

            # if lower bound is lower and upper bound is higher
            elif (num[0] < conv[0]) and (num[1] > conv[1]):
                updated_nums.append([conv[0] + conv[2], conv[1] + conv[2]])
                check_nums.append([num[0], conv[0] - 1])
                check_nums.append([conv[1] + 1, num[1]])

            else:
                check_nums.append(num)

        nums = check_nums

    if nums:
        updated_nums.extend(nums)

    return updated_nums


def get_smallest_location_number_part_2(
    nums: list[int], seed_mapping: dict
) -> int:
    for lookup in seed_mapping.values():
        nums = apply_conversions(nums, lookup)
    return min(n[0] for n in nums)


if __name__ == "__main__":
    tic = time.time()
    almanac = get_input("test_input.txt")
    seeds = [int(s.strip()) for s in almanac[0].split(":")[-1].split(" ") if s]
    seed_mapping = build_mapping_dict(almanac[1:])
    print(f"Part 1 (test) took {round(time.time() - tic, 6)}s")
    print(get_smallest_location_number(seeds, seed_mapping))

    tic = time.time()
    almanac = get_input("input.txt")
    seeds = [int(s.strip()) for s in almanac[0].split(":")[-1].split(" ") if s]
    seed_mapping = build_mapping_dict(almanac[1:])
    print(f"Part 1 took {round(time.time() - tic, 6)}s")
    print(get_smallest_location_number(seeds, seed_mapping))

    tic = time.time()
    almanac = get_input("test_input.txt")
    seeds = [int(s.strip()) for s in almanac[0].split(":")[-1].split(" ") if s]
    seeds = get_seed_numbers_part_2(seeds)
    seed_mapping = build_mapping_dict(almanac[1:])
    print(f"Part 2 (test) took {round(time.time() - tic, 6)}s")
    print(get_smallest_location_number_part_2(seeds, seed_mapping))

    tic = time.time()
    almanac = get_input("input.txt")
    seeds = [int(s.strip()) for s in almanac[0].split(":")[-1].split(" ") if s]
    seeds = get_seed_numbers_part_2(seeds)
    seed_mapping = build_mapping_dict(almanac[1:])
    print(f"Part 2 took {round(time.time() - tic, 6)}s")
    print(get_smallest_location_number_part_2(seeds, seed_mapping))
