"""
Day 8 solve
"""


f = list(open('puzzle_in.txt', 'r'))
items = [(f_.replace('\n', '')) for f_ in f]


def run_accumulator(instructions):

    indexes = []
    accumulator = []
    i = 0

    while len(indexes) == len(set(indexes)):

        indexes.append(i)

        split_instruction = instructions[i].split(' ')

        if split_instruction[0] == 'acc':
            accumulator.append(int(split_instruction[1]))
            i += 1

        elif split_instruction[0] == 'jmp':
            i += int(split_instruction[1])

        else:
            i += 1

    # need this to remove the last instruction which repeats the first if 
    # anything was added to the accumulator
    if instructions[indexes[-1]].split(' ')[0] == 'acc':
        return accumulator[:-1]

    return accumulator


print(sum(run_accumulator(items)))


def run_accumulator_check(instructions):
    """
    Update function above to return False if stuck in infinite loop and 
    accumulator value if it can run all the way through
    """

    indexes = []
    accumulator = []
    i = 0

    while len(indexes) == len(set(indexes)):

        if i >= len(instructions):
            return accumulator

        indexes.append(i)

        split_instruction = instructions[i].split(' ')

        if split_instruction[0] == 'acc':
            accumulator.append(int(split_instruction[1]))
            i += 1

        elif split_instruction[0] == 'jmp':
            i += int(split_instruction[1])

        else:
            i += 1

    return False


def fix_accumulator(instructions):
    """
    Now run through possible changes to instructions that might result in the
    instructions running properly
    """

    for i, instruction in enumerate(instructions):
        
        split_instruction = instruction.split(' ')

        if split_instruction[0] == 'jmp':

            instructions[i] = f'nop {split_instruction[1]}'
            
            if accumulator:=run_accumulator_check(instructions):
                return accumulator

            instructions[i] = f'jmp {split_instruction[1]}'

        elif split_instruction[0] == 'nop':

            instructions[i] = f'jmp {split_instruction[1]}'

            if accumulator:=run_accumulator_check(instructions):
                return accumulator
            
            instructions[i] = f'nop {split_instruction[1]}'

    return False


print(sum(fix_accumulator(items)))
