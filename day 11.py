state_matrix = [[list(i) for i in open('puzzle_inputs/puzzle_input_day_11.txt').read().split('\n')],
                [list(i) for i in open('puzzle_inputs/puzzle_input_day_11.txt').read().split('\n')]]

# state_matrix = [[list(i) for i in open('tests/test_day_11.txt').read().split('\n')]]
# state_matrix.append([list(i) for i in open('tests/test_day_11.txt').read().split('\n')])
print(id(state_matrix[0]), id(state_matrix[1]))

occup_list = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1]]
matrix_dim = len(state_matrix[0]), len(state_matrix[0][0])
print(state_matrix)
print(state_matrix[0][0][0])
static = False


def print_matrix(matrix):
    for i in matrix:
        print(i)
    print('\n','\n')


def occupied_seat_count(x, y, matrix_index):
    global occup_list
    global matrix_dim
    global state_matrix
    nb_neighbours = 0
    for i in occup_list:
        if not ((0 <= x + i[0] < matrix_dim[0]) and (0 <= y + i[1] < matrix_dim[1])):
            continue
        if state_matrix[matrix_index][x+i[0]][y+i[1]] == '#':
            nb_neighbours += 1
            if nb_neighbours > 3:
                return nb_neighbours
    return nb_neighbours

def visible_seat_count(x, y, matrix_index):
    global occup_list
    global matrix_dim
    global state_matrix
    nb_neighbours = 0
    for i in occup_list:
        k = 1
        while True:
            if not ((0 <= x + i[0]*k < matrix_dim[0]) and (0 <= y + i[1]*k < matrix_dim[1])):
                break
            if state_matrix[matrix_index][x+i[0]*k][y+i[1]*k] == '#':
                nb_neighbours += 1
                if nb_neighbours > 4:
                    return nb_neighbours
                break
            if state_matrix[matrix_index][x+i[0]*k][y+i[1]*k] == 'L':
                break
            k += 1

    return nb_neighbours


def refresh(index_matrix):
    global state_matrix
    change = False
    i = 0
    for line in state_matrix[index_matrix]:
        j = 0
        for seat in line:
            if seat == '.':
                j += 1
                continue
            elif seat == 'L':
                seats = visible_seat_count(i, j, index_matrix)
                if seats == 0:
                    state_matrix[1-index_matrix][i][j] = '#'
                    change = True
                else:
                    state_matrix[1-index_matrix][i][j] = 'L'

            elif seat == '#':
                seats = visible_seat_count(i, j, index_matrix)
                if seats > 4:
                    state_matrix[1-index_matrix][i][j] = 'L'
                    change = True
                else:
                    state_matrix[1-index_matrix][i][j] = '#'

            j += 1
        i += 1
    return change


index = 1
while True:
    if not refresh(index):
        break
    #print_matrix(state_matrix[index])
    print(state_matrix[0]==state_matrix[1])
    index = 1 - index

print_matrix(state_matrix[1])
print_matrix(state_matrix[0])


result = 0
for i in state_matrix[index]:
    for j in i:
        result += (j == '#')

print(result)
