file_line = open('tests/day_10_test_2.txt').read().split('\n')
adapters = [0] + [int(i) for i in file_line]
adapters.sort()
adapters += [adapters[-1] + 3]
liste_fixe = [[0, 0]]
for e in range(1, len(adapters) - 1):
    i = min(4, len(adapters) - e)
    if adapters[e + 1] - adapters[e - 1] > 3:
        liste_fixe.append([adapters[e], e])
liste_fixe.append([adapters[-1], len(adapters) - 1])
print(adapters)
print(liste_fixe)
partitions = []
for i in range(len(liste_fixe)-1):
    if liste_fixe[i+1][1] - liste_fixe[i][1] == 1:
        continue
    new_partition = adapters[liste_fixe[i][1]:liste_fixe[i+1][1]+1]
    partitions.append(new_partition)

print(partitions)
for partition in partitions:
    for i in range(1,len(partition)+ 1 - 2):