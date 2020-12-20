rules, my_ticket, nearby_tickets = open('puzzle_inputs/puzzle_input_day_16.txt').read().split('\n\n')
my_ticket = [int(i) for i in my_ticket.split(':\n')[1].split(',')]
rules_list = [[[int(j) for j in i.split('-')] for i in rule.split(': ')[1].split(' or ')] for rule in rules.split('\n')]
tickets_list: list = nearby_tickets.split(':\n')[1].split('\n')

s = nearby_tickets.split(':\n')[1].replace('\n', ',').split(',')
numbers = [int(i) for i in s]

result = 0
nb_remove = 0
for n in numbers:
    for rule in rules_list:
        for intervalle in rule:
            if intervalle[0] <= n <= intervalle[1]:
                break
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break
    else:
        result += n
        nb_remove += 1
# print(result)  # part 1
i = 0
j = 0
to_remove_tickets = []
while i < len(numbers):
    for rule in rules_list:
        for intervalle in rule:
            if intervalle[0] <= numbers[i] <= intervalle[1]:
                break
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break
    else:
        to_remove_tickets.append(tickets_list[j])
        j += 1
        print(j)
        i += 20 - (i % 20)
        continue
        # i -= 1
    i += 1
    if not i % 20:
        j += 1
        print(j)
print(to_remove_tickets)
for i in to_remove_tickets:
    tickets_list.remove(i)
tickets_list = [[int(j) for j in i.split(',')] for i in tickets_list]


def entry_correspond_rule(entry, rule):
    for intervalle in rule:
        if intervalle[0] <= entry <= intervalle[1]:
            break
    else:
        return False
    return True


match_matrix = [[True] * 20 for i in range(20)]

for ticket in tickets_list:
    for i in range(len(ticket)):
        for j in range(len(rules_list)):
            if not entry_correspond_rule(ticket[i], rules_list[j]):
                # if i == 0:
                # breakpoint()
                match_matrix[j][i] = False
print('______________________________________________________________________________________________________________')
for line in match_matrix:
    print(line)
print('______________________________________________________________________________________________________________')

rule_index_dico = {}
to_attribute_rules_index = [i for i in range(len(rules_list))]
while len(rule_index_dico.keys()) < len(rules_list):
    for rule_index in to_attribute_rules_index:
        if sum(match_matrix[rule_index]) == 1:
            attributed_index = match_matrix[rule_index].index(True)
            rule_index_dico[rule_index] = attributed_index
            to_attribute_rules_index.remove(rule_index)
            for i in to_attribute_rules_index:
                match_matrix[i][attributed_index] = False
            break

print(rule_index_dico)
result = 1
for i in range(6):
    result *= my_ticket[rule_index_dico[i]]

print(result)
