powers=[]
for a in range(1,100):
    for b in range(1,100):
        powers.append(a**b)
print(max([sum([int(digit) for digit in str(power)]) for power in powers]))