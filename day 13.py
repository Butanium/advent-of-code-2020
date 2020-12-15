from math import prod

wait_time, offset_list = 1000340, '13,x,x,x,x,x,x,37,x,x,x,x,x,401,x,x' \
                                  ',x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,19,x,x,x,23,x,x,x,x,x,2' \
                                  '9,x,613,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,' \
                                  'x,x,x,x,x,x,x,x,x,x,x,x,x,x,41'.replace(',', '')
offset_list = '1789,37,47,1889'
bus = [int(i) for i in offset_list.split(',') if i.isdigit()]
digit = False
offsets = [0]

offset = 1

for i in range(len(str(bus[0])), len(offset_list)):
    if offset_list[i].isdigit() and not digit:
        offsets.append(offset)
        offset += 1
        digit = True
    if offset_list[i] == 'x':
        digit = False
        offset += 1
    if offset_list[i] == ',':
        digit = False
times = [0] * len(offsets)
# print(bus)
# print(offsets)
# exit()

while True:
    mini = min(times)
    index = times.index(mini)
    times[index] += bus[index]
    if max(times) > 754518:
        breakpoint()
    l = [times[i] - times[0] == offsets[i] for i in range(1, len(times))]
    s = sum(l)
    if s == len(times) - 1:
        print(min(times))
        break


def prime_number_generator():
    prime_list = [2]
    n = 2
    yield 2
    while 1:
        n += 1
        is_prime = True
        for prime_number in prime_list:
            if n % prime_number == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(n)
            yield n


prime_generator = prime_number_generator()
prime_list = [next(prime_generator)]


def decomp(n):
    x = n
    factor_list = dict()
    i = 0
    while x >= prime_list[i]:
        if x % prime_list[i] == 0:
            x /= prime_list[i]
            if prime_list[i] in factor_list.keys():
                factor_list[prime_list[i]] += 1
            else:
                factor_list[prime_list[i]] = 1
        else:
            i += 1
            if i >= len(prime_list):
                prime_list.append(next(prime_generator))
    return factor_list


def ppcm(numbers):
    decomp_list = [decomp(n) for n in numbers]
    factors = {}
    for decomposition in decomp_list:
        for i in decomposition:
            if i in factors.keys():
                if decomposition[i] > factors[i]:
                    factors[i] = decomposition[i]
            else:
                factors[i] = decomposition[i]
    return prod([i * factors[i] for i in factors])


print(ppcm([17,13+2,19+3]))

# best_bus = 13
# best_score = 25  # > 13
# for bus in bus_list:
#     c = 0
#     while c < wait_time:
#         c += bus
#     if c - wait_time < best_score:
#         best_bus = bus
#         best_score = c - wait_time
# print(best_bus * best_score)
