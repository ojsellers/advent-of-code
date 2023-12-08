"""
Day 7 solve
"""


import numpy as np


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]


def get_outer_bags(bags, colour):
    """
    Get outer bags
    """

    outer_bags = []

    for bag in bags:

        split_bag = bag.split(' contain ')

        if colour in split_bag[1]:

            outer_bags.append(split_bag[0][:-1])

            outer_bags += get_outer_bags(bags, split_bag[0][:-1])


    return outer_bags


outer_bags = get_outer_bags(items, 'shiny gold bag')

print(len(np.unique(outer_bags)))


def get_bags_inside(bags, colour):
    """
    Get bags inside my outer bag
    """

    number_of_bags = 0

    for bag in bags:

        split_bag = bag.split(' contain ')

        if colour in split_bag[0][:-1]:

            contents = split_bag[1].replace('.', '')
            split_contents = contents.split(', ')

            quantities = [int(s) for s in contents.split() if s.isdigit()]
            number_of_bags += sum(quantities)

            for i, quant in enumerate(quantities):

                col = split_contents[i].replace(f'{quant} ', '')

                if col[-1] == 's':
                    col = col[:-1]

                number_of_bags += quant * get_bags_inside(bags, col)

    return number_of_bags


print(get_bags_inside(items, 'shiny gold bag'))