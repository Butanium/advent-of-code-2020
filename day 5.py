file = open('puzzle_inputs/puzzle_input_day_5.txt')
siege_ids = file.read().split('\n')


def get_siege_id(dichotomie_string):
    row = [0, 127]
    column = [0, 7]
    for i in range(7):

        if dichotomie_string[i] == 'F':
            row[1] = (sum(row)) // 2

        else:
            row[0] = (sum(row)) // 2 + 1
    if dichotomie_string[6] == 'F':
        row = row[0]
    else:
        row = row[1]
    for i in range(3):
        if dichotomie_string[7 + i] == 'L':
            column[1] = (column[0] + column[1]) // 2
        else:
            column[0] = (column[0] + column[1]) // 2 + 1

    if dichotomie_string[9] == 'L':
        column = column[0]
    else:
        column = column[1]
    return 8*row + column

max = 0
siege_ids_list = []
for i in siege_ids:
    s = get_siege_id(i)
    siege_ids_list.append(s)
    max = (max > s) * max + (max <= s) * s

print(siege_ids_list)
missing_sieges = []
for i in range(max):
    if i not in siege_ids_list:
        missing_sieges.append(i)

print(missing_sieges)

