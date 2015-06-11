from sympy import isprime
def per_eq(a,b):
    if sorted(list(str(a)))==sorted(list(str(b))):
        return True
    return False
for start in range(1000,9999):
    for step in range(1,3333+1):
        if isprime(start) and isprime(start+step) and isprime(start+2*step) and per_eq(start,start+step) and per_eq(start,start+2*step):
            print(start,start+step,start+2*step)