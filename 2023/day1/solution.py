DIGIT_MAPPING = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}


def get_input(filename: str) -> list[str]:
    with open(filename, "r+") as f:
        data = f.read()
    return data.splitlines()


def get_calibration_sum_1(data: list[str]) -> int:
    return sum(
        int(digits[0] + digits[-1])
        for d in data
        if (digits := [_d for _d in d if _d.isdigit()])
    )


def replace_word_digits(value: str) -> str:
    for k, v in DIGIT_MAPPING.items():
        value = value.replace(k, v)
    return value


def get_calibration_sum_2(data: list[str]) -> int:
    return sum(
        int(digits[0] + digits[-1])
        for d in data
        if (digits := [_d for _d in replace_word_digits(d) if _d.isdigit()])
    )


if __name__ == "__main__":
    data = get_input("input.txt")

    print(get_calibration_sum_1(data))

    print(get_calibration_sum_2(data))
