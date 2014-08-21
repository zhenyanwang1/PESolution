from math import sqrt


def F(n):
    return int(((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5)))


val = 0
pos = 1
while True:
    num = F(pos)
    if num <= 4000000:
        if num % 2 == 0:
            val += num
    else:
        break
    pos += 1
print(val)