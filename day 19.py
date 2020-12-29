from typing import List

sep = '__________________________________________'
rule_lines, messages_lines = open('tests/day_19_test.txt').read().split('\n\n')
# rule_lines = '''0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"'''
#
# messages_lines = '''ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb'''

part_2 = True
rules = {
    int(i.split(': ')[0]): [list(map(int, j.split(' '))) if '"a"' not in j and '"b"' not in j else j[1] for j in
                            i.split(': ')[1].split(' | ')] for i in rule_lines.split('\n')}

messages = messages_lines.split('\n')
test_file = open('tests/sorted_day_19_test.txt', 'w')
for i in range(max(rules.keys()) + 1):
    if i in rules.keys():
        test_file.write(str(i) + ': ' + str(rules[i])[1:-1:] + '\n')


def is_message_valid(string, s_index, r_index, valid_rules = ()):
    if not valid_rules:
        valid_rules = []
    valid_rules += [r_index]

    if isinstance(rules[r_index][0][0], str):
        if s_index >= len(string) and part_2:
            # print('out of range')
            return True, 0, valid_rules
        return string[s_index] == rules[r_index][0][0], 1, valid_rules

    for rule_set in rules[r_index]:
        attempt_rules = valid_rules.copy()
        test_len = 0
        for rule in rule_set:
            t, length, liste  = is_message_valid(string, s_index + test_len, rule, attempt_rules)
            if not t:
                break
            attempt_rules = liste
            if not length:
                return True, test_len, attempt_rules
            test_len += length
        else:
            break
    else:
        return False, test_len, attempt_rules
    if r_index == 0 and test_len < len(string):
        return False, 'not all characters matched'
    return True, test_len, attempt_rules


test_valid_messages = '''bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''.split('\n')

result = 0
caca = 'aaaabbaaaabbaaa'
r, l, rule_list = is_message_valid('aaaabbaaaabbaaa', 0, 0)
print(r, rule_list)
print(sep)
a = [rules[i][0] for i in rule_list if type(rules[i][0])==str]
string = ""
print(string.join(a))
# for message in messages:
#     if message == 'aaaabbaaaabbaaa':
#         breakpoint()
#     r,_ = is_message_valid(message, 0, 0)
#     result += r
#     if r and message not in test_valid_messages:
#         print(message)

print(result)
