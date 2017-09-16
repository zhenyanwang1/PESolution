from sympy import Rational,fraction
r=Rational(1/2)
n=0
for i in range(1000):
    r=1/(2+r)
    print(r+1)
    if len(str((r+1).p))>len(str((r+1).q)):
        n+=1
print(n)