def get_input(filename: str) -> list[str]:
    with open(filename, "r+") as f:
        data = f.read()
    return data.splitlines()


def get_points(cards: list[str]) -> int:
    points = 0
    for card in cards:
        card = card.split(": ")[-1].split("|")
        winning = [n.strip() for n in card[0].split(" ") if n]
        have = [n.strip() for n in card[1].split(" ") if n]
        if won := [n for n in winning if n in have]:
            points += 2 ** (len(won) - 1)
    return int(points)


def get_n_wins(card: str) -> int:
    winning = [n.strip() for n in card[0].split(" ") if n]
    have = [n.strip() for n in card[1].split(" ") if n]
    return len([n for n in winning if n in have])


def update_card_count(
    i: int, cards: dict[int, int], card_count: dict[int, int]
) -> dict:
    wins = cards[i]
    for j in range(1, wins + 1):
        card_count[i + j] += 1
        card_count = update_card_count(i + j, cards, card_count)
    return card_count


def get_copies(cards: list[str]) -> list[str]:
    cards = {
        i + 1: get_n_wins(card.split(": ")[-1].split("|"))
        for i, card in enumerate(cards)
    }
    card_count = {i + 1: 1 for i in range(len(cards))}
    for i in range(1, len(cards) + 1):
        card_count = update_card_count(i, cards, card_count)
    return sum(card_count.values())


if __name__ == "__main__":
    cards = get_input("test_input.txt")
    print(get_points(cards))

    cards = get_input("input.txt")
    print(get_points(cards))

    cards = get_input("test_input.txt")
    print(get_copies(cards))

    cards = get_input("input.txt")
    print(get_copies(cards))
