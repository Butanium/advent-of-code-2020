from copy import deepcopy

slices = {0: [list(i) for i in open('puzzle_inputs/puzzle_input_day_17.txt').read().split('\n')]}
# slices = {0: [list(i) for i in open('tests/day_17.txt').read().split('\n')]}

active = '#'
inactive = '.'
nb_of_slice = 0

x_len = len(slices[0][0])
y_len = len(slices[0])


def get_inactive_slice():
    return [['.' for i in range(len(slices[0][0]))] for j in range(len(slices[0]))]


def get_permutations(nb_of_entry, nb_of_state):
    return [[int(i / nb_of_state ** j) % nb_of_state for j in range(nb_of_entry)] for i in
            range(nb_of_state ** nb_of_entry)]


neighbours_coordinates = get_permutations(3, 3)
neighbours_coordinates.remove([1, 1, 1])
neighbours_coordinates = [[i - 1 for i in j] for j in neighbours_coordinates]
print(neighbours_coordinates)


def get_active_neighbours(x, y, z, f_slices: dict):

    keys = list(f_slices.keys())
    nb_alive_neighbours = 0
    for xyz in neighbours_coordinates:
        if abs(z + xyz[2]) in keys and 0 <= x + xyz[0] < len(f_slices[0][0]) and 0 <= y + xyz[1] < len(f_slices[0]):
            nb_alive_neighbours += (f_slices[abs(z + xyz[2])][y + xyz[1]][x + xyz[0]] == active)
            if nb_alive_neighbours == 4:
                return 4
    return nb_alive_neighbours


def update_reactor():
    global nb_of_slice
    global x_len
    global y_len
    x_len += 2
    y_len += 2
    nb_of_slice += 1
    old_slices = deepcopy(slices)
    for i in range(nb_of_slice):
        for j in slices[i]:
            j.insert(0, '.')
            j.append('.')
        slices[i].insert(0, ['.'] * x_len)
        slices[i].append(['.'] * x_len)
    slices[nb_of_slice] = get_inactive_slice()
    for z in range(0, nb_of_slice + 1):
        for x in range(x_len):
            for y in range(y_len):
                nb_neighbours = get_active_neighbours(x-1, y-1, z, old_slices)
                if nb_neighbours == 3:
                    slices[z][y][x] = active
                elif z == nb_of_slice or x >= x_len - 1 or y >= y_len - 1 or x == 0 or y == 0:
                    continue
                elif old_slices[z][y-1][x-1] == active and nb_neighbours == 2:
                    continue
                else:
                    slices[z][y][x] = inactive

result = 0
for i in range(6):
    update_reactor()
for i in slices.keys():
    print('z = ' + str(i))
    for j in slices[i]:
        print(j)
        for h in j:
            result += (h == '#')*(1 + (i != 0))
    print('___________________________________________')

print(result)
# don't forget * 2
