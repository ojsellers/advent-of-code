"""
Day 5 solve
"""


import math


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]


def get_split(ticket, upper, upper_char):

    lower = 0

    for i in range(len(ticket)):

        if ticket[i] == upper_char:
            upper = upper - math.ceil((upper - lower) / 2)

        else:
            lower = lower + math.ceil((upper - lower) / 2)

    assert upper == lower

    return upper


def get_row(ticket):
    """
    Get the row of the ticket
    """

    return get_split(ticket, 127, 'F')


def get_column(ticket):
    """
    Get column of ticket
    """

    return get_split(ticket, 7, 'L')


def get_seat_ids(tickets):

    seat_ids = []

    for ticket in tickets:

        row = get_row(ticket[:7])

        col = get_column(ticket[-3:])

        seat_ids.append(row * 8 + col)

    return seat_ids


def find_missing_id(seat_ids):

    seat_ids.sort()

    for i in range(seat_ids[0], seat_ids[-1]+1):

        if i not in seat_ids:
            return i
            


seat_ids = get_seat_ids(items)
print(max(seat_ids))

print(find_missing_id(seat_ids))