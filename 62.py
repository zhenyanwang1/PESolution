from collections import defaultdict
from itertools import count


def is_cube(x):
    x = abs(x)
    return int(round(x ** (1. / 3))) ** 3 == x


def same_digits(*kargs):
    max_length = max([len(str(karg)) for karg in kargs])
    chrll = [sorted(list(str(karg) + "0" * (max_length - len(str(karg))))) for karg in kargs]
    for chrl in chrll:
        if chrl != chrll[0]:
            return False
    return True


print(same_digits(12300, 123, 13200))
print(same_digits(14300, 134, 41030))
LIMIT = 5

cubes = []

perms = defaultdict(set)

for n in count(1):
    cubes.append(n ** 3)
    anas = [cube for cube in cubes if same_digits(cube, n ** 3)]
    if len(anas) == 5:
        if all([len(str(ana)) == len(str(anas[0])) for ana in anas]):
            print("SUCCESS", len(anas), min(anas), anas)
            break
        else:
            print("PARTIAL", len(anas), min(anas), anas)
    if len(anas) > 2:
        print("FAIL", n, len(anas))
