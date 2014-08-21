from sympy import isprime
pos=1
val=1
while True:
    if isprime(val):
        if pos!=10001:
            pos+=1
        else:
            print(val)
            break
    val+=1