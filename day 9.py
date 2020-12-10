file = open('puzzle_inputs/puzzle_input_day_9.txt')
file_lines = file.read().split('\n')


def is_sum_of_25(index):
    global file_lines
    print('e')
    for j in range(25):
        for h in range(j, 25):
            if int(file_lines[index]) == int(file_lines[j + index - 25]) + int(file_lines[h + index - 25]):
                return True
    return False


# for i in range(24, len(file_lines)):
#     if not is_sum_of_25(i):
#         print(file_lines[i],i)
#         break
n = 32321523
for i in range(len(file_lines) - 1):
    int_sum = int(file_lines[i])
    j = i + 1
    end = ''
    maxi = mini = int_sum
    while int_sum < n:
        h = int(file_lines[j])
        maxi = (h > maxi) * h + (h <= maxi) * maxi
        mini = (h < mini) * h + (h >= mini) * mini
        int_sum += h
        end = file_lines[j]
        j += 1
    if int_sum == n:
        print(mini+maxi)
        exit()
