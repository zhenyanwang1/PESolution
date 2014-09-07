def rcl(n):
    initial=1%n
    remainder=initial
    remainders=[initial]
    while True:
        if not remainder * 10 % n in remainders:
            remainder=remainder * 10 % n
            remainders.append(remainder)
        else:
            return len(remainders)
rcls={}
for i in range(1,1000):
    rcls[i]=rcl(i)
print(sorted(rcls.items(),key=lambda l:l[1],reverse=True)[0][0])