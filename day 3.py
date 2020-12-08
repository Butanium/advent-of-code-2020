from sys import exit


def extract_file(file_name, nb_of_line=0):
    file = open(file_name, 'r')
    if not nb_of_line:
        my_lines = file.readlines()
    else:
        my_lines = file.readlines(nb_of_line)
    to_return = [[i[j] for j in range(len(i) - 1)] for i in my_lines]
    return to_return


file_lines = extract_file('puzzle_inputs/puzzle_input_day_3.txt')


def check_slope(right, down):
    x = 0
    y = 0
    trees = 0
    c = 0
    while y < len(file_lines):
        file_line_list = list(file_lines[y])
        if file_line_list[x] == '#':
            trees += 1
            st = '\033[31m' + file_line_list[x] + '\033[0m'
        else:
            st = '\033[34m' + file_line_list[x] + '\033[0m'

        print(str(file_line_list[:x:]) + st + str(file_line_list[x + 1::]))
        c += 1
        y += down
        x += right
        if x > len(file_lines[0]) - 1:
            x = x % (len(file_lines[0]))

    return trees


downs = [1, 1, 1, 1, 2]
rights = [1, 3, 7, 5, 1]
r = 1
for i in range(len(downs)):
    r *= check_slope(rights[i], downs[i])

print(r)
