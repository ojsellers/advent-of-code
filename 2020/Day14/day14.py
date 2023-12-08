"""
Day 14
"""


import numpy as np


f = list(open('puzzle_in.txt', 'r'))
items = [f_.replace('\n', '') for f_ in f]


def run_program(program):

    memory = {}

    for prog in program:

        split_prog = prog.split(' = ')

        if split_prog[0] == 'mask':
            mask = split_prog[1]

        else:
            address = split_prog[0]
            memory[address] = apply_mask(mask, split_prog[1])

    return memory


def apply_mask(mask, content):

    mask = list(mask)
    content = list('{:036b}'.format(int(content)))

    for i in range(len(mask)):

        if mask[i] == 'X':
            mask[i] = content[i]

    return int(f'0b{int("".join(mask))}', 2)


memory = run_program(items)
print(sum([val for val in memory.values()]))


# Part 2
def run_program_2(program):
    """
    For part 2 have to run slightly differently as could take along time to
    compute all the combinations of floating bits. So first apply the mask to
    the binary address with updated rules and without doing anything with X
    bits, then add all combinations of floating bits to memory
    """
    memory = {}

    for prog in program:

        split_prog = prog.split(' = ')

        if split_prog[0] == 'mask':
            mask = split_prog[1]

        else:
            address = split_prog[0].split('[')[1].split(']')[0]
            address = apply_mask_2(mask, address)
            memory[address] = int(split_prog[1])

    return apply_floating_bits(memory)


def apply_mask_2(mask, address):
    """
    This applies the mask with second rule set to a certain address without
    taking floating bits (X) into account to produce an initialised memory
    """
    mask = list(mask)
    address = list('{:036b}'.format(int(address)))

    for i in range(len(mask)):

        if mask[i] == '0':
            mask[i] = address[i]

    return ''.join(mask)


def apply_floating_bits(memory):
    """
    This function is now applied on the memory to account for combinations of
    floating X bits, returning the final memory configuration after program
    """
    new_memory = {}

    for key in memory.keys():

        new_key = list(key)

        # get indices of X bits
        x_i = [i for i, x in enumerate(key) if x == 'X']

        # get combinations of possible X bit values using binary formatting
        combs = ['{:0{}b}'.format(i, len(x_i)) for i in range(2**len(x_i))]

        # apply combinations to address and add each to memory
        for comb in combs:
            for i in range(len(comb)):
                new_key[x_i[i]] = comb[i]
            new_memory[''.join(new_key)] = memory[key]

    return new_memory


memory = run_program_2(items)
print(sum([val for val in memory.values()]))
