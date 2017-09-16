i = 1
while True:
    strings = [sorted([int(digit) for digit in str(mult * i)]) for mult in [2, 3, 4, 5, 6]]
    oks = [s == strings[0] for s in strings]
    if all(oks):
        break
    i += 1
print(i)
