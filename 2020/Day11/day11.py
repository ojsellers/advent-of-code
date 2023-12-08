"""
Day 11 solve
"""


import numpy as np
import copy


f = list(open('puzzle_in.txt', 'r'))
items = [f_.replace('\n', '') for f_ in f]


def prepare_grid(items):

    grid = np.zeros((99, 100))
    # grid = np.zeros((12, 12))

    for i, item in enumerate(items):

        item = item.replace('.', '0')
        item = item.replace('L', '1')
        item = item.replace('#', '2')

        row = [int(i) for i in item]

        row.insert(0, 0)
        row.append(0)

        grid[i+1] = row

    return grid


def compute_iteration(grid):

    grid_copy = copy.deepcopy(grid)

    for j in range(1, len(grid[0])-1):
        for i in range(1, len(grid[:, 0])-1):

            grid_copy[i, j] = apply_rules(grid[i-1:i+2, j-1:j+2])

    return grid_copy


def apply_rules(mini_grid):

    occupied = 0

    for i in range(3):
        for j in range(3):

            if mini_grid[i, j] == 2:
                occupied += 1

    if occupied == 0 and mini_grid[1, 1] == 1:
        return 2

    elif occupied >= 5 and mini_grid[1, 1] == 2:
        return 1

    return mini_grid[1, 1]


def run_iterations(grid):

    for i in range(100):

        new_grid = compute_iteration(grid)

        if np.all(new_grid==grid):
            return new_grid

        grid = new_grid

    return False
            

grid = prepare_grid(items)

# pt1_grid = run_iterations(grid)
# print(np.count_nonzero(pt1_grid==2))


# # PART 2

directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (1, -1), (0, 1), (1, 0), (1, 1))

def compute_iteration_2(grid):

    grid_copy = copy.deepcopy(grid)

    for j in range(1, len(grid[0])-1):
        for i in range(1, len(grid[:, 0])-1):

            grid_copy[i, j] = apply_rules_2(grid, i, j)

    return grid_copy


def apply_rules_2(grid, i, j):

    occupied = 0

    for direction in directions:

        val = get_closest_seat(direction, grid, i, j)
        if val == 2:
            occupied += 1

    if occupied == 0 and grid[i, j] == 1:
        return 2

    elif occupied >= 5 and grid[i, j] == 2:
        return 1

    return grid[i, j]


def get_closest_seat(direction, grid, i, j):

    condition = False

    while condition == False:

        i += direction[0]
        j += direction[1]
        
        if i == 0 or i == len(grid[:,0])-1:
            return 0

        elif j == 0  or j == len(grid[0])-1:
            return 0 

        if grid[i, j] == 1:
            return 1

        elif grid[i, j] == 2:
            return 2

    
def run_iterations_2(grid):

    for i in range(100):

        new_grid = compute_iteration_2(grid)

        if np.all(new_grid==grid):
            return new_grid

        grid = new_grid

    return False


pt2_grid = run_iterations_2(grid)
print(np.count_nonzero(pt2_grid==2))