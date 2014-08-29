def chain(n):
    while True:
        yield n
        if n == 1:
            break
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1


ret = []
for n in range(1, 1000000):
    ret.append((n, len(list(chain(n)))))
print(max(ret, key=lambda datum: datum[1])[0])