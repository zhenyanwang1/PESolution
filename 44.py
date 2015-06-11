from gmpy2 import is_square
from math import sqrt
def p(n):
    return n*(3*n-1)/2
def has_sol(a,b,c):
    d=b**2-4*a*c
    if d<0:
        return False
    if not is_square(int(d)):
        return False
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    if (x1>0 and x1.is_integer()) or (x2>0 and x2.is_integer()):
        return True
    return False
ns=[]
for j in range(1,5000):
    for k in range(j+1,5000):
        s=p(k)+p(j)
        d=p(k)-p(j)
        D=abs(p(j)-p(k))
        if has_sol(3,-1,-2*s) and has_sol(3,-1,-2*d):
            ns.append((j,k))
            print((j,k))
for n in ns:
    print(n,abs(p(n[0])-p(n[1])))