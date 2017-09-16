from itertools import count, permutations

from sympy import sieve,isprime


def cond(l):
    print(l)
    for p in permutations(l, 2):
        if not isprime(int("".join([str(x) for x in p]))):
            return False
    return True

sums=[129977413]
for a in count(2):
    if sieve[a]>min(sums):
        break
    for b in count(a + 1):
        if sum([sieve[v] for v in [a, b]])>min(sums):
            break
        if not cond([sieve[v] for v in [a, b]]):
            continue
        for c in count(b + 1):
            if sum([sieve[v] for v in [a, b,c]]) > min(sums):
                break
            if not cond([sieve[v] for v in [a, b, c]]):
                continue
            for d in count(c + 1):
                if sum([sieve[v] for v in [a, b,c,d]]) > min(sums):
                    break
                if not cond([sieve[v] for v in [a, b, c, d]]):
                    continue
                for e in count(d + 1):
                    if sum([sieve[v] for v in [a, b, c, d,e]]) >= min(sums):
                        break
                    if not cond([sieve[v] for v in [a, b, c, d, e]]):
                        continue
                    sums.append(sum([sieve[v] for v in [a, b, c, d, e]]))
print(min(sums))