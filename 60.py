from itertools import permutations
from time import monotonic

from sympy import isprime, primerange

st = monotonic()


def test(l):
    for p in permutations(l, 2):
        if not isprime(int("".join([str(x) for x in p]))):
            return False
    return True


MAX = 10000

cache = {}
for x in primerange(2, MAX):
    if not x in cache:
        cache[x] = set()
    for y in primerange(2, MAX):
        if test([x, y]):
            cache[x].add(y)

cache = {k: v for k, v in cache.items() if len(v) > 0}
print(len(cache.keys()))
print(cache)

ls = []

for a in cache.keys():
    for b in cache[a]:
        for c in cache[b]:
            if not (c in cache[a] and c in cache[b]):
                continue
            for d in cache[c]:
                if not (d in cache[a] and d in cache[b] and d in cache[c]):
                    continue
                for e in cache[d]:
                    if not (e in cache[a] and e in cache[b] and e in cache[c] and e in cache[d]):
                        continue
                    else:
                        ls.append(sum(set(sorted([a, b, c, d, e]))))
print(min(ls))
et = monotonic()
print("TIME", et - st)
