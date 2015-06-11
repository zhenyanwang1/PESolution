#Too slow in CPython,PyPy is a must
from math import sqrt
pp={p:[] for p in range(1,1000+1)}
for p in range(1,1000+1):
    for b in range(1,1000+1):
        for a in range(1,b+1):
            if a+b>p-a-b and a-b<p-a-b and a**2+b**2==(p-a-b)**2:
                print(p)
                pp[p].append((a,b,int(sqrt(a**2+b**2))))
for p in sorted(list(filter(lambda p: len(p[1])!=0,pp.items())),key=lambda p:len(p[1])):
    print(p)