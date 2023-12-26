def get_input(filename: str):
    with open(filename, "r+") as f:
        data = f.read()
    return data.splitlines()


def rotate_platform(platform: list[str]) -> list[str]:
    return ["".join(row[::-1]) for row in zip(*platform)]


def tilt_platform(platform: list[str]) -> list[str]:
    return [
        "#".join("".join(sorted(group)) for group in row.split("#"))
        for row in platform
    ]


def get_summed_load(platform: list[str]) -> int:
    return sum(
        i + 1
        for row in platform
        for i, value in enumerate(row)
        if value == "O"
    )


def run_cycles(platform: list[str], num_cycles: int) -> list[str]:
    seen_platforms_lookup = {}
    for i in range(1, num_cycles + 1):
        for _ in range(4):
            platform = rotate_platform(platform)
            platform = tilt_platform(platform)

        if platform in list(seen_platforms_lookup.values()):
            break

        seen_platforms_lookup[i] = platform

    loop_start = [
        k for k, v in seen_platforms_lookup.items() if v == platform
    ][0]
    if i == loop_start:
        return seen_platforms_lookup[i]
    return seen_platforms_lookup[
        (num_cycles - loop_start) % (i - loop_start) + loop_start
    ]


if __name__ == "__main__":
    platform = get_input("test_input.txt")
    platform = rotate_platform(platform)
    platform = tilt_platform(platform)
    print(get_summed_load(platform))

    platform = get_input("input.txt")
    platform = rotate_platform(platform)
    platform = tilt_platform(platform)
    print(get_summed_load(platform))

    platform = get_input("test_input.txt")
    platform = run_cycles(platform, 1000000000)
    platform = rotate_platform(platform)
    print(get_summed_load(platform))

    platform = get_input("input.txt")
    platform = run_cycles(platform, 1000000000)
    platform = rotate_platform(platform)
    print(get_summed_load(platform))
