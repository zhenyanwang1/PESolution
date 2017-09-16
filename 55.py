def rev(n):
    return int(str(n)[::-1])


def pal(s):
    return s == s[::-1]


def pal_int(n):
    return pal(str(n))


def lychrel(n):
    sum = n
    iteration = 0
    while (not pal_int(sum) or iteration == 0) and iteration < 50:
        sum += rev(sum)
        iteration += 1
    if pal_int(sum):
        return False
    return True


n = 0
for i in range(1, 10000):
    if lychrel(i):
        n += 1
print(n)
