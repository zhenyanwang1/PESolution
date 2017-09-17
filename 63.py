from itertools import count
def is_power(x,p):
    x = abs(x)
    return int(round(x ** (1. / p))) ** p == x

def ndigits(n):
    for x in count(1):
        powered=x**n
        if powered>=10**n:
            break
        if 10**(n-1)>powered:
            continue
        if len(str(powered))==n:
            yield powered
total=0
for x in count(1):
    l=list(ndigits(x))
    total+=len(l)
    print(x,len(l),l)
    if len(l)==0:
        print(total)
        break