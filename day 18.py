from math import prod

operations = [i.replace(' ', '') for i in open('puzzle_inputs/puzzle_input_day_18.txt').read().split('\n')]
sep = '______________________________________________'


def get_bracket_result(op: str, start_index):
    if op[start_index] == '(':
        result, i = get_bracket_result(op, start_index + 1)
        i += start_index
    else:
        result = int(op[start_index])
        i = start_index + 1
    while op[i] != ')':
        if op[i] == '*':
            if op[i + 1] != '(':
                result *= int(op[i + 1])
                i += 2
            else:
                r, l = get_bracket_result(op, i + 2)
                result *= r
                i += l + 1
        else:
            if op[i + 1] != '(':
                result += int(op[i + 1])
                i += 2
            else:
                r, l = get_bracket_result(op, i + 2)
                result += r
                i += l + 1
    return result, i - start_index + 2  # return result and len of the bracket


def get_result(op: str):
    if op[0] == '(':
        result, i = get_bracket_result(op, 1)
    else:
        result = int(op[0])
        i = 1
    while i < len(op) - 1:
        if op[i] == '*':
            if op[i + 1] != '(':
                result *= int(op[i + 1])
                i += 2
            else:
                r, l = get_bracket_result(op, i + 2)
                result *= r
                i += l + 1
        else:
            if op[i + 1] != '(':
                result += int(op[i + 1])
                i += 2
            else:
                r, l = get_bracket_result(op, i + 2)
                result += r
                i += l + 1
    return result


# solution = sum(get_result(operation) for operation in operations)

def remove_additions(op_l):
    i = 1
    while i < len(op_list) - 1 and '+' in op_l:
        if op_list[i] == '+' and isinstance(op_list[i - 1], int) and isinstance(op_list[i + 1], int):
            op_list[i + 1] += op_list[i - 1]
            op_list.pop(i)
            op_list.pop(i - 1)
        else:
            i += 1


caca = ''
solution = 0
# operations = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'.replace(' ','')]
for operation in operations:
    op_list = [int(i) if i.isdigit() else i for i in operation]
    remove_additions(op_list)
    while '(' in op_list:
        for i in range(len(op_list) - 1, -1, -1):
            if op_list[i] == '(':
                break
        r = op_list[i+1]
        if op_list[i + 2] == ')':
            end = i+2
        else:
            end = 0
            for j in range(i+3, len(op_list)-1, 2):
                r *= op_list[j]
                if op_list[j+1] == ')':
                    end = j+1
                    break
            if not end:
                caca = 'caca'
                end = len(op_list)-1
        for h in range(i, end):
            op_list.pop(i)
        op_list[i] = r
        remove_additions(op_list)
    solution += prod(op_list[::2])

print(solution)