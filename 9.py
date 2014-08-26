for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if not a < b < c:
                continue
            if a + b + c != 1000:
                continue
            if a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)
                break