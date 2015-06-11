from sympy import isprime
i=1
def pan(n,s):
    if len(set(s))<len(s):
        return False
    if len(s)>10:
        return False
    for d in "".join([str(i) for i in range(1,n+1)]):
        if not d in s:
            return False
    return True
while True:
    if isprime(i) and pan(len(str(i)),str(i)):
        print(i)
    i+=1