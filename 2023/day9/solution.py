def get_input(filename: str):
    with open(filename, "r+") as f:
        data = f.read()
    data = [
        [int(v) for v in line.split(" ")] for line in data.splitlines() if line
    ]
    return data


def get_sequence_diffs(sequence: list[int]) -> int:
    sequences = [sequence]
    while True:
        next_seq = [
            sequences[-1][i] - sequences[-1][i - 1]
            for i in range(1, len(sequences[-1]))
        ]
        sequences.append(next_seq)
        if len(set(next_seq)) == 1:
            return sequences


def reverse_sequences_and_get_next_val(sequences: list[list[int]]) -> int:
    for i in range(1, len(sequences)):
        this_val = sequences[-i][-1] + sequences[-i - 1][-1]
        sequences[-i - 1].append(this_val)
    return this_val


def sum_next_sequence_values(sequences: list[list[int]]) -> int:
    return sum(
        reverse_sequences_and_get_next_val((get_sequence_diffs(sequence)))
        for sequence in sequences
    )


def reverse_sequences_and_get_past_val(sequences: list[list[int]]) -> int:
    for i in range(1, len(sequences)):
        this_val = sequences[-i - 1][0] - sequences[-i][0]
        sequences[-i - 1].insert(0, this_val)
    return this_val


def sum_past_sequence_values(sequences: list[list[int]]) -> int:
    return sum(
        reverse_sequences_and_get_past_val((get_sequence_diffs(sequence)))
        for sequence in sequences
    )


if __name__ == "__main__":
    sequences = get_input("test_input.txt")
    print(sum_next_sequence_values(sequences))

    sequences = get_input("input.txt")
    print(sum_next_sequence_values(sequences))

    sequences = get_input("test_input.txt")
    print(sum_past_sequence_values(sequences))

    sequences = get_input("input.txt")
    print(sum_past_sequence_values(sequences))
