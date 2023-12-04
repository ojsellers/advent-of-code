import numpy as np

LOOKUP = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
COLOURS = (
    "red",
    "green",
    "blue",
)


def get_input(filename: str) -> list[str]:
    with open(filename, "r+") as f:
        data = f.read()
    return data.splitlines()


def is_game_possible(game: str) -> bool:
    game = game.split(":")[-1].replace(";", ",")
    for hand in game.split(","):
        hand = hand.strip().split(" ")
        if int(hand[0]) > LOOKUP[hand[1]]:
            return False
    return True


def get_solution_1(games: list[str]) -> int:
    return sum(i + 1 for i, game in enumerate(games) if is_game_possible(game))


def get_game_power(game: str) -> int:
    min_numbers = {}
    game = game.split(":")[-1].replace(";", ",")
    for hand in game.split(","):
        hand = hand.strip().split(" ")
        colour = hand[1]
        number = int(hand[0])
        if number > min_numbers.get(colour, 0):
            min_numbers[colour] = number
    return np.product(list(min_numbers.values()))


def get_solution_2(games: list[str]) -> int:
    return sum(get_game_power(game) for game in games)


if __name__ == "__main__":
    games = get_input("input.txt")
    # games = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    # ]

    print(get_solution_1(games))
    print(get_solution_2(games))
