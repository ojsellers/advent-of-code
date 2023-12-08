"""
Day 15 solve
"""


f = list(open('puzzle_in.txt', 'r'))
items = [f_.replace('\n', '') for f_ in f]
items = items[0].split(',')
items = [int(item) for item in items]


def play_game(sequence, req_num=2020):

    while len(sequence) < req_num:

        last_num = sequence[-1]

        appearance_i = [i for i, num in enumerate(sequence[:-1]) if num == last_num]

        if len(appearance_i) == 0:
            sequence.append(0)

        else:
            sequence.append(len(sequence)-1 - max(appearance_i))

    return sequence


sequence = play_game(items)
print(sequence[-1])


def play_game_faster(sequence, req_num=30000000):
    """
    Right, now need to optimise to make the game run through faster to get up
    to the 30000000th number in a reasonable time. To do so going to use a
    dict to keep track of the last time each number appeared in the game, where
    keys are the number and the values are the last appearance. Theeturn Then
    """
    game = {num: i + 1 for i, num in enumerate(sequence[:-1])}
    count = len(sequence)
    last_num = sequence[-1]

    while count < req_num:

        if last_num not in game.keys():
            game[last_num] = count
            last_num = 0

        else:
            old_i = game[last_num]
            game[last_num] = count
            last_num = count - old_i

        count += 1

    return game, last_num


game, last_num = play_game_faster(items)
print(last_num)
