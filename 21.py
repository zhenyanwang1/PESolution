import sympy
def d(n):
    return sum(sympy.divisors(n)[:-1])
l=set()
for i in range(1, 10000):
    if d(d(i))==i and d(i)!=i:
        l.add(d(i))
        l.add(i)
print(sum(l))