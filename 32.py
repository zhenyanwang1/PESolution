from sympy import divisors
from itertools import product


def pandigital(s):
    if len(s) != 9:
        return False
    for d in "123456789":
        if not d in s:
            return False
    return True


sum = 0
for i in range(1, 750000):
    divs = divisors(i)
    for pair in product(divs, repeat=2):
        if pair[0] * pair[1] == i and pandigital("".join((str(pair[0]), str(pair[1]), str(i)))):
            sum += i
            print(pair[0], pair[1], i, "SUM=", sum)
            break
