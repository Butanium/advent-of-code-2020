file_line = open('puzzle_inputs/puzzle_input_day_10.txt').read().split('\n')
adapters = [0] + [int(i) for i in file_line]
adapters.sort()
adapters += [adapters[-1] + 3]
liste_fixe = [[0, 0]]
for e in range(1, len(adapters) - 1):
    i = min(4, len(adapters) - e)
    if adapters[e + 1] - adapters[e - 1] > 3:
        liste_fixe.append([adapters[e], e])
liste_fixe.append([adapters[-1], len(adapters) - 1])
partitions = []
maxi = 0
for i in range(len(liste_fixe) - 1):
    if liste_fixe[i + 1][1] - liste_fixe[i][1] == 1:
        continue
    new_partition = adapters[liste_fixe[i][1]:liste_fixe[i + 1][1] + 1]
    maxi = (maxi >= len(new_partition)) * maxi + len(new_partition) * (maxi < len(new_partition))
    partitions.append(new_partition)
partition_scores = []
for partition in partitions:
    len_part = len(partition)
    if len_part == 3:
        partition_scores.append(2)
        continue
    if len_part == 4:
        partition_scores.append(1+2+1)
        continue
    if len_part == 5:
        partition_scores.append(1+3+3)
result = 1
for i in partition_scores:
    result *= i
print(result)
    # for nb_permut_to_achieve in range(1, len(partition) + 1 - 2):  # 1 à len(partition) -2 possibilités on rajoute 1
    #     # afin d'inclure le nom
    #     for start_index in range(1, len(partition) - nb_permut_to_achieve):
    #         are_removed = [False] * len(partition)
    #         for increment in range(0, nb_permut_to_achieve):
    #             if not are_removed[start_index + increment]:
    #                 pass
    #             elif are_removed[start_index + increment - 2]:
    #                 pass
