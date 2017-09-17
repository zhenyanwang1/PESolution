def rcl(n):
    remainder = 10 % n
    remainders = []
    while True:
        remainder = remainder * 10 % n
        if remainder == 0:
            return 0
        if not remainder in remainders:
            remainders.append(remainder)
        else:
            return len(remainders)


rcls = {}
for i in range(1, 1000):
    rcls[i] = rcl(i)
print(sorted(rcls.items(), key=lambda l: l[1], reverse=True)[0][0])
