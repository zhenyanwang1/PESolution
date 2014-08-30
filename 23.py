import sympy


def d(n):
    return sum(sympy.divisors(n)[:-1])


isabnum = []
for num in range(1, 28123 + 1):
    isabnum.append(d(num) > num)
abnums = [num for num in range(28123 + 1) if d(num) > num]
total = 0
for i in range(1, 28123 + 1):
    ok = False
    for abnum in abnums:
        if abnum >= i:
            break
        if not isabnum[i - abnum - 1]:
            ok = False
        else:
            ok = True
            break
    if ok == False:
        total += i
print(total)