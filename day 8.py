file = open('puzzle_inputs/puzzle_input_day_8.txt').read().split('\n')
file_lines = [i.split(' ') for i in file]
print(file_lines)
index_list = []
accumulator = 0


def is_finish(fill_list=False):
    global index_list
    global file_lines
    bool_list = [False] * len(file_lines)
    global accumulator
    accumulator = 0
    index = 0
    while index != len(file_lines) - 1:
        if bool_list[index]:
            return False
        bool_list[index] = True
        if fill_list:
            index_list.append(index)
        if file_lines[index][0] == 'jmp':
            string = file_lines[index][1]
            index += ((string[0] == '-') * -2 + 1) * int(string[1:])
            continue
        if file_lines[index][0] == 'acc':
            string = file_lines[index][1]
            accumulator += ((string[0] == '-') * -2 + 1) * int(string[1:])
        index += 1
    return True


is_finish(True)

for i in index_list[::-1]:
    instr = file_lines[i][0]
    new_instr = 'nop'
    if instr == 'nop':
        new_instr = 'jmp'
    file_lines[i][0] = new_instr
    if is_finish():
        print(accumulator)
        break
    else:
        file_lines[i][0] = instr

print(accumulator)
