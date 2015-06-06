S = 0
for i in range(1, 5000000):
    if i == sum([d ** 5 for d in [int(c) for c in str(i)]]):
        S += i
        print(i)
print(S)