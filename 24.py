import itertools
gen=itertools.permutations([n for n in range(0,10)])
for i in range(1000000-1):
    next(gen)
ret=next(gen)
print("".join([str(n) for n in ret]))