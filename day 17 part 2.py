from copy import deepcopy
from time import process_time

dimensions = {0: {0: [list(i) for i in open('puzzle_inputs/puzzle_input_day_17.txt').read().split('\n')]}}
# dimensions = {0: {0: [list(i) for i in open('tests/day_17.txt').read().split('\n')]}}
# print(dimensions)
# exit()
active = '#'
inactive = '.'
nb_of_slice = 0
nb_of_dimensions = 0
x_len = len(dimensions[0][0][0])
y_len = len(dimensions[0][0])

t = process_time()

def get_permutations(nb_of_entry, nb_of_state):
    return [[int(i / nb_of_state ** j) % nb_of_state for j in range(nb_of_entry)] for i in
            range(nb_of_state ** nb_of_entry)]


neighbours_coordinates = get_permutations(4, 3)
neighbours_coordinates.remove([1, 1, 1, 1])
neighbours_coordinates = [[i - 1 for i in j] for j in neighbours_coordinates]


def get_active_neighbours(x, y, z, w, f_dimensions: dict):
    nb_alive_neighbours = 0
    for xyzw in neighbours_coordinates:
        if abs(w + xyzw[3]) in f_dimensions.keys() and abs(z + xyzw[2]) in f_dimensions[
            abs(w + xyzw[3])].keys() and 0 <= x + \
                xyzw[0] < len(f_dimensions[0][0][0]) and 0 <= y + xyzw[1] < len(f_dimensions[0][0]):
            nb_alive_neighbours += (
                    f_dimensions[abs(w + xyzw[3])][abs(z + xyzw[2])][y + xyzw[1]][x + xyzw[0]] == active)
            if nb_alive_neighbours == 4:
                return 4
    return nb_alive_neighbours


def update_reactor():
    global nb_of_dimensions
    global dimensions
    global nb_of_slice
    global x_len
    global y_len
    x_len += 2
    y_len += 2
    nb_of_dimensions += 1
    nb_of_slice += 1
    old_dimensions = deepcopy(dimensions)
    for d in range(nb_of_dimensions):
        slices = dimensions[d]
        for i in range(nb_of_slice):
            for j in slices[i]:  # ajout des débuts et fin de ligne
                j.insert(0, '.')
                j.append('.')
            slices[i].insert(0, ['.'] * x_len)  # ajout de 2 lignes vides
            slices[i].append(['.'] * x_len)
        slices[nb_of_slice] = [['.'] * x_len for _ in range(y_len)]  # ajout d'une épaisseur
    dimensions[nb_of_dimensions] = {s: [['.'] * x_len for _ in range(y_len)] for s in range(nb_of_slice + 1)}
    #  ajout d'une dimension
    for w in range(nb_of_dimensions + 1):
        for z in range(0, nb_of_slice + 1):
            for x in range(x_len):
                for y in range(y_len):
                    nb_neighbours = get_active_neighbours(x - 1, y - 1, z, w, old_dimensions)
                    if nb_neighbours == 3:
                        dimensions[w][z][y][x] = active
                    elif w == nb_of_dimensions or z == nb_of_slice or \
                            x >= x_len - 1 or y >= y_len - 1 or x == 0 or y == 0:
                        continue
                    elif old_dimensions[w][z][y - 1][x - 1] == active and nb_neighbours == 2:
                        continue
                    else:
                        dimensions[w][z][y][x] = inactive


result = 0
for i in range(6):
    update_reactor()
    print('dimension ' + str(i) + ' achieved')

for j in dimensions.keys():
    slices_tpr = dimensions[j]
    for i in slices_tpr.keys():
        # print('w = ' + str(j) + '  z = ' + str(i))
        for k in slices_tpr[i]:
            # print(k)
            for h in k:
                result += (h == '#') * (1 + (i != 0)) * (1 + (j != 0))
        # print('___________________________________________')
# print(dimensions)
print(result)
print(process_time()-t)
# don't forget * 2
