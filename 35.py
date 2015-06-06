from itertools import permutations
from sympy import isprime

rot = lambda s: s[1:] + s[0]


def cir(n):
    if not isprime(n):
        return False
    s = str(n)
    for _ in range(len(s)):
        if not isprime(int(s)):
            return False
        s = rot(s)
    return True


l = []
for i in range(1, 1000000 + 1):
    if cir(i):
        l.append(i)
        print(i)
print("TOTAL=", len(l))

# A AB ABC ABCD
#  BA BCA BCDA
#     CAB CDAB
#         DABC