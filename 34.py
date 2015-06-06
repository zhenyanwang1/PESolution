from sympy import factorial

for i in range(1, 2000000):
    if i == sum([factorial(int(c)) for c in str(i)]):
        print(i)