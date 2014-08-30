def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
pos=1
for n in fib():
    if len(str(n))==1000:
        print(pos)
        break
    pos+=1