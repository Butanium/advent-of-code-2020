instructions = open('puzzle_inputs/puzzle_input_day_12.txt').read().split('\n')
instructions = '''F10
N3
F7
R90
F11'''.split('\n')
north = 0
east = 0
coordinates = ['E', 'N', 'W', 'S']
coords_lens = [0] * 4
facing_coordinate = 0
waypoint = [10, 1]


def turn_v2(rot_direction, front, turn_rate):
    turn_rate = rot_direction * turn_rate // 90
    r = front + turn_rate
    if r > 3:
        r %= 4
    elif r < -3:
        r = 4 + r
    return r


# for instruction in instructions:
#     op = ''
#     nb = ''
#     for char in instruction:
#         if char.isdigit():
#             nb += char
#         else:
#             op += char
#     nb = int(nb)
#     if op == 'N' or op == 'S':
#         north += nb * (1 - 2 * (op == 'S'))
#     elif op == 'E' or op == 'W':
#         east += nb * (1 - 2 * (op == 'W'))
#     elif op == 'L' or op == 'R':
#         facing_coordinate = turn_v2(1 if op == 'L' else -1, facing_coordinate, nb)
#     elif op == 'F':
#         coords_lens[facing_coordinate] += nb


for instruction in instructions:
    op = ''
    nb = ''
    for char in instruction:
        if char.isdigit():
            nb += char
        else:
            op += char
    nb = int(nb)
    if op == 'N' or op == 'S':
        waypoint[1] += nb * (1 - 2 * (op == 'S'))
    elif op == 'E' or op == 'W':
        waypoint[0] += nb * (1 - 2 * (op == 'W'))
    elif op == 'L' or op == 'R':
        if nb == 180:
            waypoint[0] *= -1
            waypoint[1] *= -1
        if nb == 90 or nb == 270:
            if (op == 'L') != (nb == 270):
                waypoint[0], waypoint[1] = -1*waypoint[1], waypoint[0]
            else:
                waypoint[0], waypoint[1] = waypoint[1], -1*waypoint[0]
    elif op == 'F':
        north += nb*waypoint[1]
        east += nb*waypoint[0]
print(abs(north)+abs(east))