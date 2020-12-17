instructions = open('puzzle_inputs/puzzle_input_day_14.txt').read().split('\n')

instructions = [i.replace('=', '').split('  ') for i in instructions]
instructions = [[int(i[0][4:-1:]), int(i[1])] if i[0] != 'mask' else i for i in instructions]
memory = dict()


def get_mask(mask):
    return {len(mask) - 1 - i: int(mask[i]) for i in range(len(mask)) if mask[i] != 'X'}


def get_mask_2(mask):
    return [len(mask) - 1 - i for i in range(len(mask)) if mask[i] == '1'], \
           [len(mask) - 1 - i for i in range(len(mask)) if mask[i] == 'X']


def get_36bits_bin(nb):
    bin_nb = list(bin(nb))
    return [0 if i < 36 + 2 - len(bin_nb) else int(bin_nb[-36 + len(bin_nb) + i]) for i in range(36)]


def bin_to_int(bin_nb):
    return sum([2 ** (len(bin_nb) - i - 1) * bin_nb[i] for i in range(len(bin_nb))])


def apply_mask(f_mask: dict, nb):
    bin_nb = get_36bits_bin(nb)
    print(bin_nb)
    for i in range(len(bin_nb)):
        if i in f_mask.keys():
            bin_nb[36 - 1 - i] = f_mask[i]
    return bin_to_int(bin_nb)


# part 1
# for instruction in instructions:
#     if type(instruction[0]) != int:
#         mask = get_mask(instruction[1])
#     else:
#         memory[instruction[0]] = apply_mask(mask, instruction[1])


def apply_mask_to_memory(f_mask: list, x_index, memory_adress, item):
    binary_memory_adress = get_36bits_bin(memory_adress)
    global memory
    memories = [[int(i / 2 ** j) % 2 for j in range(len(x_index))] for i in range(2 ** len(x_index))]
    for i in f_mask:
        binary_memory_adress[36 - 1 - i] = 1
    for mem in memories:
        b_list = binary_memory_adress
        for i in range(len(x_index)):
            b_list[36-1-x_index[i]] = mem[i]
        memory[bin_to_int(b_list)] = item


for instruction in instructions:
    if type(instruction[0]) != int:
        mask, x_list = get_mask_2(instruction[1])
    else:
        apply_mask_to_memory(mask, x_list, instruction[0], instruction[1])

result = sum([memory[i] for i in memory])
print(memory.items())
print(memory.keys())
print(result)
