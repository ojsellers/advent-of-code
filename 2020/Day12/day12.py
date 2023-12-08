"""
Day 12 solve
"""


import numpy as np


f = list(open('puzzle_in.txt', 'r'))
items = [f_.replace('\n', '') for f_ in f]


ship_direction = 90
direction_map = {'N': (0, 1), 'S': (0,-1), 'E': (1, 0), 'W': (-1, 0), 'F': (1, 0)}


def get_distance(instructions, pt):

    east_i = 0
    north_j = 0

    for instruction in instructions:

        if pt == 1:
            i, j = apply_instructions(instruction[0], instruction[1:])

        else:
            i, j = apply_instructions_2(instruction[0], instruction[1:])

        east_i += i
        north_j += j

    return round(abs(east_i) + abs(north_j))


def apply_instructions(direction, value):
    """
    Here using ship direction angle to respond to changes in direction and 
    update the value for F in the direction_map
    """
    global ship_direction
    global direction_map

    if direction == 'L':
        ship_direction -= int(value)

    elif direction == 'R':
        ship_direction += int(value)

    else:
        return direction_map[direction][0]*int(value), direction_map[direction][1]*int(value)

    direction_map['F'] = (np.sin(np.radians(ship_direction)), np.cos(np.radians(ship_direction)))

    return 0, 0

print(get_distance(items, pt=1))


# # part 2

# update F direction map
direction_map['F'] = [10, 1]

def apply_instructions_2(direction, value):
    """
    Here now I am just applying the angle directly to a change in coordinates
    of the waypoint (F in direction_map) rather than keeping track of the ship 
    direction
    """
    global direction_map

    waypoint = direction_map['F']

    if direction == 'F':
        return waypoint[0]*int(value), waypoint[1]*int(value)

    elif direction == 'L':
        rot_angle = np.radians(int(value))
        waypoint = [waypoint[0]*np.cos(rot_angle) - waypoint[1]*np.sin(rot_angle), 
                    waypoint[0]*np.sin(rot_angle) + waypoint[1]*np.cos(rot_angle)]

    elif direction == 'R':
        rot_angle = np.radians(int(value))
        waypoint = [waypoint[0]*np.cos(rot_angle) + waypoint[1]*np.sin(rot_angle), 
                    -waypoint[0]*np.sin(rot_angle) + waypoint[1]*np.cos(rot_angle)]  

    else:
        waypoint[0] += direction_map[direction][0] * int(value)
        waypoint[1] += direction_map[direction][1] * int(value)

    direction_map['F'] = waypoint

    return 0, 0


print(get_distance(items, pt=2))