from sympy import isprime
def cut(s,direction=1):
    if direction==1:
        return s[1:]
    elif direction==-1:
        return s[:-1]
def allprime(l):
    for i in l:
        if not isprime(i):
            return False
    return True
sum=0
for i in range(1,1000000):
    if not isprime(i) or len(str(i))==1:
        continue
    s=str(i)
    l=[]
    for _ in range(1,len(s)+1):
        l.append(s)
        s=cut(s,1)
    s=str(i)
    for _ in range(1,len(s)+1):
        l.append(s)
        s=cut(s,-1)
    if allprime(l):
        sum+=i
        print(i)
print("SUM=",sum)