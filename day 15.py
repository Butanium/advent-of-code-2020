from time import process_time
t = process_time()
first_numbers = [20,9,11,0,1,2]
last_index_numbers = {first_numbers[i]: i+1 for i in range(len(first_numbers)-1)}
print(last_index_numbers)
last_nb = first_numbers[-1]
from time import process_time
t = process_time()
for i in range(len(first_numbers)+1, 30000001):
    if last_nb in last_index_numbers.keys():
        new_nb = i-1 - last_index_numbers[last_nb]
        last_index_numbers[last_nb] = i - 1
        last_nb = new_nb
    else:
        last_index_numbers[last_nb] = i-1
        last_nb = 0
print(last_nb)
print(process_time()-t)