from sympy import isprime
squares=[i**2 for i in range(1,1000)]
def conj(n):
    for square in squares:
        if isprime(n-2*square):
            return True
    return False
i=3
while True:
    if isprime(i):
        i+=2
        continue
    if not conj(i):
        print(i)
        break
    i+=2