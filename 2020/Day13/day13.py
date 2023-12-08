"""
Day 13 solve
"""


f = list(open('puzzle_in.txt', 'r'))
items = [f_.replace('\n', '') for f_ in f]


def get_bus(notes):

    possible_buses = {}

    my_time = int(notes[0])
    bus_info = notes[1].split(',')
    bus_info = [int(val) for val in bus_info if val != 'x']

    for info in bus_info:

        remainder = my_time % info

        possible_buses[info] = - remainder + info

    return possible_buses


possible_buses = get_bus(items)
min_key = min(possible_buses, key=possible_buses.get)
print(min_key * possible_buses[min_key])


# part 2
def get_timegaps(notes):

    mods, remains = [], []

    bus_info = notes[1].split(',')

    for i, info in enumerate(bus_info):

        if info != 'x':
            mods.append(int(info))
            remains.append(int(info)-i)

    return mods, remains


def find_timestamp(mods, remains):
    """
    Chinese remainder theorem to calculate x for a series of co-prime mods
    leading to any set of remainders
    """
    prod = 1
    sum = 0

    for mod in mods:
        prod *= mod

    for mod, remain in zip(mods, remains):
        y = prod // mod
        sum += remain * y * mul_inv(y, mod)

    return sum % prod


def mul_inv(a, b):
    """
    This function uses Euclids extended algorithm to calculate the inverse
    of y % mod. Got this from Rosetta code website
    """
    b0 = b
    x0, x1 = 0, 1

    if b == 1:
        return 1

    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0: x1 += b0

    return x1


mods, remains = get_timegaps(items)
print(mods, remains)
print(find_timestamp(mods, remains))
