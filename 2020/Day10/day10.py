"""
Day 10 solve
"""


import numpy as np


f = list(open('puzzle_in.txt', 'r'))
items = [int(f_.replace('\n', '')) for f_ in f]
items.sort()

items.append(max(items)+3)
items.insert(0, 0)


def get_chain(jolts):

    differences = []

    for i in range(len(jolts) - 1):

        differences.append(jolts[i+1] - jolts[i])

    return differences


differences = get_chain(items)
# print(differences.count(1) * differences.count(3))


def count_arrangements(jolts):

    arrangements = 1

    groups = get_exchangable_groups(jolts)

    print(groups)

    for group in groups:

        arrangements *= group_possibilities(group)

    num_groups = len([group for group in groups if len(group) >= 3])

    print(num_groups)

    return arrangements


def get_exchangable_groups(jolts):

    groups = []
    last_i = 0

    for i in range(0, len(jolts) - 1):

        if jolts[i+1] - jolts[i] == 3:
            groups.append(jolts[last_i:i+1])
            last_i = i + 1

    groups.append(jolts[last_i:])    

    return groups


def group_possibilities(group):
    """
    Using Tribonacci (0,0,1,1,2,4,7,...) sequence
    """

    nums = [0, 0, 1]
    
    for i in range(len(group)-1):
        nums.append(sum(nums[-3:]))

    return nums[-1]


print(count_arrangements(items))