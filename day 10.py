file_line = open('tests/day_10_test_2.txt').read().split('\n')
adapters = [0] + [int(i) for i in file_line]
from math import factorial

# b = min(adapters)
# ada = adapters.copy()
# ada.sort()
# print(ada)
# adapters.remove(b)
# diff_3 = b == 3
# diff_1 = b == 1
# lenn = len(adapters)
# for i in range(0, lenn):
#     a = min(adapters)
#     adapters.remove(a)
#     if a - b == 3:
#         diff_3 += 1
#     elif a - b == 1:
#         diff_1 += 1
#         print(a)
#     elif a - b > 3:
#         print('caca')
#     b = a
#
# print((diff_3+1)*diff_1)
# print(diff_1)
adapters.sort()
removable_adaptors = []
removable_doubles = []
if adapters[2] <= 3:
    removable_adaptors = [adapters[1]]
# if adapters[2] <= 3:
#     removable_adaptors.append([adapters[0],adapters[1]])
nb_double = 0
print(adapters)
for i in range(2, len(adapters) - 2):
    l = []
    if adapters[i + 1] - adapters[i - 2] == 3:
        pass
        #continue
    if removable_doubles:
        if adapters[i] in removable_doubles[-1]:
            continue
    #     removable_adaptors.append([adapters[i-1]] + l)
    if adapters[i + 2] - adapters[i - 1] == 3:
        removable_doubles.append([adapters[i]] + [adapters[i + 1]])
        nb_double += 1
        continue
    if adapters[i + 1] - adapters[i - 1] <= 3:
        l.append(adapters[i])
        removable_adaptors.append(adapters[i])


# def get_permutation_from_index(index, nb_permutations, last_element, permutation_count=0):
#     global removable_adaptors
#     global removable_doubles
#     if nb_permutations == 0:
#         return 1
#     if [removable_adaptors[index], removable_adaptors[index+1]] in removable_doubles:
#         get_permutation_from_index(index+1, nb_permutations - 1, index, permutation_count)
#     for i in range(index + 2, len(removable_adaptors)):
#         permutation_count += get_permutation_from_index(i, nb_permutations - 1, index, permutation_count)


def get_permutation_from_index(index, nb_permutations, last_element=-2):
    global removable_adaptors
    global removable_doubles
    permutation_count = 0
    if nb_permutations == 0:  # si plus de permutations alors renvoyer 1
        return 1
    if index + nb_permutations > len(
            removable_adaptors) - 1:  # si impossible d'obtenir le nb de permutations renvoyer 0
        return 0
    if removable_adaptors[index + 1] - removable_adaptors[index] > 1 \
            or [removable_adaptors[index], removable_adaptors[index + 1]] in removable_doubles and \
            removable_adaptors[index] - last_element > 1:  # s'il y a plus de 1 d'écart entre ce numéro et le suivant
        # ou que l'on peut se permettre d'enlever les 2 et qu'il n'y a pas 1 d'écart avec le
        # précédent truc enlevé (on ne peut pas enlever 3 éléments d'affilée
        permutation_count += get_permutation_from_index(index + 1, nb_permutations - 1, removable_adaptors[index])
    for i in range(index + 2,
                   len(removable_adaptors) - nb_permutations + 1):  # on part de deux index plus loins jusqu'au dernier
        # pouvant marcher
        permutation_count += get_permutation_from_index(i, nb_permutations - 1, removable_adaptors[index])
    return permutation_count


print(removable_adaptors)
print(removable_doubles)


def calculate_nb_permutation(nb_free_adapters, nb_double_adapter):
    free_permut = 2 ** nb_free_adapters - 1
    nb_double_permut = 2 ** (nb_free_adapters + 1 + nb_double_adapter) - 1
    return free_permut+nb_double_permut

print(calculate_nb_permutation(len(removable_adaptors),len(removable_doubles)))

exit()
result = 1 + len(removable_adaptors)
for i in range(1, len(removable_adaptors)):  # nb de permutations possibles
    for j in range(len(removable_adaptors) - i):  # tous les éléments à partir desquels on peut commencer
        a = get_permutation_from_index(j, i)
        print(a)
        result += a
    print('########', str(i) + ' permutations', '########')

print('result : ', result)

'''1 2 3 4 5'''
