import sympy


def tri(n):
    return sum(range(1, n + 1))


n = 1
while True:
    num = tri(n)
    if sympy.divisor_count(num) >= 500:
        print(num)
        break
    n += 1
