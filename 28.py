pos = 1
sum = 1
print(1)
for i in range(1, 501):
    for _ in range(4):
        pos += 2 * i
        print(pos)
        sum += pos
print("SUM=", sum)