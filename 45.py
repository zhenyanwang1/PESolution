from gmpy2 import is_square
from math import sqrt
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
def t(n):
    return n*(n+1)/2
def is_t(n):
    return has_sol(1,1,-2*n)
def is_p(n):
    return has_sol(3,-1,-2*n)
def is_h(n):
    return has_sol(2,-1,-n)
i=286
while True:
    tn=t(i)
    if is_p(tn) and is_h(tn):
        print(tn)
        break
    i+=1