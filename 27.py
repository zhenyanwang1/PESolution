import sympy
ret={}
for a in range(-1000, 1000 + 1):
    for b in range(-1000, 1000 + 1):
        n=0
        while True:
            if not sympy.isprime(n**2+a*n+b):
                break
            n+=1
        ret[(a,b)]=n
ret = sorted(ret.items(), key=lambda pair: pair[1], reverse=True)
print(ret[0][0][0] * ret[0][0][1])