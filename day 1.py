from main import extract_list_from_file

puzzle_input = open('puzzle_inputs/puzzle_input_day_1.txt')

my_int = extract_list_from_file(puzzle_input, int)


for i in range(len(my_int)):
    for j in range(i+1, len(my_int)):
        for h in my_int:
            if my_int[i] + my_int[j]+h == 2020:
                result = my_int[i]*my_int[j]*h

print(result)
