# class Passport:
#     def __init__(self):
def all_elements_in():
    passport_bools = [False] * len(name_list)
    result = 0
    for line in file_lines:
        reset = True
        bus = ''
        if line == '\n':
            result += check_passport(passport_bools)
            passport_bools = [False] * len(name_list)

        for c in line:
            if c == ':':
                passport_bools[name_list.index(bus)] = True
                bus = ''
                reset = False
                continue
            if reset:
                bus += c
            if not reset and (c == ' ' or c == '\n'):
                reset = True
    result += check_passport(passport_bools)
    print(result)


file = open('puzzle_inputs/puzzle_input_day_4.txt')
file_lines = file.readlines()


def check_passport(passport_list):
    a = sum([bool(i) for i in passport_list])
    a += not passport_list[name_list.index('cid')]
    to_return = a == len(name_list)
    return to_return


name_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
hairs_chars = [str(i) for i in range(10)]
hairs_chars.extend(['a', 'b', 'c', 'd', 'e', 'f'])

eye_chars = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def check_passports_elements(passport):
    if not (2002 >= int(passport[0]) >= 1920):
        # print('2002 < '+ '\033[31m' + str(int(passport[0]))+'\033[0m'+' < 1920')
        return False
    if not (2020 >= int(passport[1]) >= 2010):
        # print('2010 < '+ '\033[31m' + str(int(passport[1]))+'\033[0m'+' < 2020')
        return False
    if not (2030 >= int(passport[2]) >= 2020):
        return False
    if not (passport[4][0] == '#'):
        return False
    if not len(passport[4]) == 7:
        return False
    for i in range(1, 7):
        if passport[4][i] not in hairs_chars:
            return False
    if passport[5] not in eye_chars:
        return False
    if len(passport[6]) != 9:
        return False
    x = passport[3][-2] + passport[3][-1]
    if x == 'cm':
        n = int(passport[3][:len(passport[3]) - 2:])
        if not (150 <= n <= 193):
            return False
    elif x == 'in':
        n = int(passport[3][:len(passport[3]) - 2:])
        if not (59 <= n <= 76):
            return False
    else:
        return False

    return True


def valid_elements():
    passport_properties = [''] * len(name_list)
    result = 0
    debug = 0
    for line in file_lines:

        reset = True
        bus = ''
        if line == '\n':
            if check_passport(passport_properties):
                x = check_passports_elements(passport_properties)
                result += x
                debug += 1
                if not x:
                    print(passport_properties)
            passport_properties = [''] * len(name_list)

        for c in line:
            if c == ':':
                index_elem = name_list.index(bus)
                bus = ''
                reset = False
                continue
            if reset:
                bus += c
            if c == ' ' or c == '\n':
                reset = True
            if not reset and c != '\n':
                passport_properties[index_elem] += c

    if check_passport(passport_properties):
        result += check_passports_elements(passport_properties)
    print(str(result) + ' debug : ' + str(debug))


valid_elements()
