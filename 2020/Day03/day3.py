"""
Day three solve
"""


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]


def get_trees(forest, across, down):

    across_i = 0
    down_i = 0
    trees = 0

    for row in range(len(forest) // down):

        if forest[down_i][across_i] == '#':
            trees += 1

        across_i += across
        if across_i > 30:
            across_i -= 31

        down_i += down

    return trees


print(get_trees(items, 3, 1))


a = get_trees(items, 1, 1)
b = get_trees(items, 3, 1)
c = get_trees(items, 5, 1)
d = get_trees(items, 7, 1)
e = get_trees(items, 1, 2)


print(a * b * c * d * e)