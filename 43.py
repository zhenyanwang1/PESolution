from itertools import permutations
def pan(s):
    if len(set(s))<len(s):
        return False
    for d in "0123456789":
        if not d in s:
            return False
    return True
ds=[2,3,5,7,11,13,17]
def fun(n):
    for i in range(1,7+1):
        if int(str(n)[i:i+3])%ds[i-1]!=0:
            return False
    return True
pans=[int("".join(s)) for s in list(filter(lambda s:s[0]!="0",list(permutations("0123456789",r=10))))]
print(len(pans))
sum=0
for i in pans:
    if fun(i):
        print(i)
        sum+=i
print("SUM",sum)