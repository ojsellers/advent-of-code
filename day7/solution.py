from collections import Counter

REPLACE = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
}
REPLACE_2 = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "T": "D",
    "9": "E",
    "8": "F",
    "7": "G",
    "6": "H",
    "5": "I",
    "4": "J",
    "3": "K",
    "2": "L",
    "J": "M",
}


def get_input(filename: str) -> list[str]:
    with open(filename, "r+") as f:
        data = f.read()
    return [line for line in data.splitlines() if line]


def get_hand_score(cards: str):
    counts = list(Counter(cards).values())
    if max(counts) > 3:
        return max(counts) + 2
    elif max(counts) == 3:
        return 5 if 2 in counts else 4
    elif max(counts) == 2:
        return 3 if counts.count(2) > 1 else 2
    return 1


def sort_hands_and_sum(hands: dict) -> int:
    scored_hands = {}
    for hand in hands:
        hand = hand.split(" ")
        scored_hands.setdefault(get_hand_score(hand[0]), {}).update(
            {"".join(REPLACE[h] for h in hand[0]): hand[1]}
        )
    scored_hands = [
        int(hand[1])
        for hands in sorted(scored_hands.items())
        for hand in sorted(hands[1].items(), reverse=True)
    ]
    return sum(h * (i + 1) for i, h in enumerate(scored_hands))


def _update_counts_with_j_count(cards, counts):
    j_count = cards.count("J")
    if j_count > 0:
        counts.remove(j_count)
        if not counts:
            return [5]
        _max = max(counts)
        counts.remove(_max)
        counts.append(_max + j_count)
    return counts


def get_hand_score_2(cards: str):
    counts = list(Counter(cards).values())
    counts = _update_counts_with_j_count(cards, counts)
    if max(counts) > 3:
        return max(counts) + 2
    elif max(counts) == 3:
        return 5 if 2 in counts else 4
    elif max(counts) == 2:
        return 3 if counts.count(2) > 1 else 2
    return 1


def sort_hands_and_sum_2(hands: dict) -> int:
    scored_hands = {}
    for hand in hands:
        hand = hand.split(" ")
        scored_hands.setdefault(get_hand_score_2(hand[0]), {}).update(
            {"".join(REPLACE_2[h] for h in hand[0]): hand[1]}
        )
    scored_hands = [
        int(hand[1])
        for hands in sorted(scored_hands.items())
        for hand in sorted(hands[1].items(), reverse=True)
    ]
    return sum(h * (i + 1) for i, h in enumerate(scored_hands))


if __name__ == "__main__":
    hands = get_input("test_input.txt")
    print(sort_hands_and_sum(hands))

    hands = get_input("input.txt")
    print(sort_hands_and_sum(hands))

    hands = get_input("test_input.txt")
    print(sort_hands_and_sum_2(hands))

    hands = get_input("input.txt")
    print(sort_hands_and_sum_2(hands))
