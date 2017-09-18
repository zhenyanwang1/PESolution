from itertools import combinations

from sympy import isprime, sieve


def gen_subs(digits):
    if isinstance(digits, str):
        digits = list(digits)
    for n in range(10):
        if digits.index("*") == 0 and n == 0:
            continue
        yield [digit if digit != "*" else str(n) for digit in digits]


class Mask:
    def __init__(self, digits):
        if isinstance(digits, str):
            digits = list(digits)
        self.digits = digits

    def __iter__(self):
        for n in range(10):
            if self.digits.index("*") == 0 and n == 0:
                continue
            yield int("".join([digit if digit != "*" else str(n) for digit in self.digits]))

    def __repr__(self):
        return "'{}'".format("".join(self.digits))


def gen_masks(n):
    digits = list(str(n))
    for x in range(1, len(digits)):
        for c in combinations(range(len(digits)), x):
            new_digits = digits[:]
            for pos in c:
                new_digits[pos] = "*"
            yield Mask(new_digits)


for p in sieve:
    fin = False
    if len(set(str(p))) == len(str(p)):
        continue
    for mask in gen_masks(p):
        total = 0
        vs = []
        for sub in mask:
            if isprime(sub):
                total += 1
                vs.append(sub)
            if total > 8:
                break
        if total == 8:
            print(p, mask,vs)
            fin = True
            break
        elif total > 6:
            print("STEP", p, mask,vs)
    if fin:
        break
