class password:
    def __init__(self, l_char, bs, s):
        self.limited_char = l_char
        self.bounds = bs
        self.string = s

    def print(self):
        indexs = [self.bounds[0]-1, self.bounds[1]-1]
        #if
        s1 = str(self.string[indexs[0]+1:indexs[1]:1])
        print(str(self.bounds) + ' ' + str(self.limited_char) + ' ' + str(self.string[:indexs[0]:1])+ '\033[31m'+
              self.string[indexs[0]]+'\033[0m'+ s1+ '\033[31m'+
              self.string[indexs[1]]+'\033[0m'+self.string[indexs[1]+1::1])

#'\033[31m'

def extract_list_from_file(file):
    my_string = file.read()
    print(my_string[-1])
    my_list = []
    limited_char = ''
    bounds = ['', '']
    s = ''
    state = 0
    c = 0
    for i in my_string:
        c+=1
        if c ==len(my_string)-3:
            print(990)
        if i == '\n' and state:
            my_list.append(password(limited_char, [int(i) for i in bounds], s))
            limited_char = ''
            bounds = ['', '']
            s = ''
            state = 0
        if i == ' ' or i == ':' or i == '-':
            state += 1
            continue
        if state < 2:
            bounds[state] += i
        if state == 2:
            limited_char = i
        if state == 4:
            s += i
    my_list.append(password(limited_char, [int(i) for i in bounds], s))
    return my_list


my_list = extract_list_from_file(open("puzzle_inputs/puzzle_input_day_2.txt"))




def check_password(pass_w: password):
    c = 0
    for i in pass_w.string:
        if i == pass_w.limited_char:
            c += 1
        if c > pass_w.bounds[1]:
            return False
    if c < pass_w.bounds[0]:
        return False
    return True


def check_password_V2(pass_w: password):
    a0 = pass_w.string[pass_w.bounds[0] - 1] == pass_w.limited_char
    a1 = pass_w.string[pass_w.bounds[1] - 1] == pass_w.limited_char
    #if a0!=a1:
       # pass_w.print()
    return a0 != a1

print(True != True)

r = 0
for p in my_list:
    r += check_password_V2(p)
print(r)
