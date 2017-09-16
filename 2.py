def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


total = 0
for x in fib():
    if x > 4000000:
        break
    if x % 2 == 0:
        total += x
        print(x)
print(total)
