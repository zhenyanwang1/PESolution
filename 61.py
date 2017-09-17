from itertools import count,permutations


def gen_with_prefix(n):
    if isinstance(n, str):
        n = int(n)
    for m in range(1, 100):
        if 10 <= n <= 99:
            yield n * 100 + m


tris = []
squs = []
pents = []
hexas = []
hepts = []
octos = []

for n in count(1):
    tri = n * (n + 1) // 2
    tris.append(tri)
    squ = n ** 2
    squs.append(squ)
    pent = n * (3 * n - 1) // 2
    pents.append(pent)
    hexa = n * (2 * n - 1)
    hexas.append(hexa)
    hept = n * (5 * n - 3) // 2
    hepts.append(hept)
    octo = n * (3 * n - 2)
    octos.append(octo)

    if all(map(lambda x: x > 10000, [tri, squ, pent, hexa, hept, octo])):
        break

print(tris)
print(squs)
print(pents)
print(hexas)
print(hepts)
print(octos)


def get_status(n):
    statuses=[]
    if n in tris:
        statuses.append(3)
    if n in squs:
        statuses.append(4)
    if n in pents:
        statuses.append(5)
    if n in hexas:
        statuses.append(6)
    if n in hepts:
        statuses.append(7)
    if n in octos:
        statuses.append(8)
    return statuses


def cull(n):
    if n in tris or n in squs or n in pents or n in hexas or n in hepts or n in octos:
        return False
    else:
        return True


for a in range(1000, 10000):
    if cull(a):
        continue
    for b in gen_with_prefix(str(a)[2:]):
        if cull(b):
            continue
        for c in gen_with_prefix(str(b)[2:]):
            if cull(c):
                continue
            for d in gen_with_prefix(str(c)[2:]):
                if cull(d):
                    continue
                for e in gen_with_prefix(str(d)[2:]):
                    if cull(e):
                        continue
                    if int(str(e)[2:]) < 10:
                        continue
                    f = int(str(e)[2:] + str(a)[:2])
                    if cull(f):
                        continue
                    l=[a,b,c,d,e,f]
                    for a1,b1,c1,d1,e1,f1 in permutations(l):
                        if a1 in tris and b1 in squs and c1 in pents and d1 in hexas and e1 in hepts and f1 in octos:
                            print(a, b, c, d, e, f, "SUM", sum([a, b, c, d, e, f]), "STAT", sorted([get_status(n) for n in [a, b, c, d, e, f]]))
                            exit()