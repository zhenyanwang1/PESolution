from math import sqrt
from gmpy2 import is_square
def t(n):
    return n(n+1)/2
def has_sol(a,b,c):
    d=b**2-4*a*c
    if d<0:
        return False
    if not is_square(d):
        return False
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    if x1>0 or x2>0:
        return True
    return False
def code(s):
    return sum([ord(c)-64 for c in s])
f=open("words.txt")
words=[word[1:-1] for word in f.read().split(",")]
codes=list(filter(lambda c:has_sol(1,1,-2*c),list(map(code,words))))
print(codes)
print(len(codes))