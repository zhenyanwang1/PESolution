# Slow in CPython, PyPy recommended
from itertools import permutations

coins = [1, 2, 5, 10, 20, 50, 100, 200]
plans = []
for a in range(200 + 1):
    for b in range(100 + 1):
        for c in range(40 + 1):
            for d in range(20 + 1):
                for e in range(10 + 1):
                    for f in range(4 + 1):
                        for g in range(2 + 1):
                            for h in range(1 + 1):
                                sum = 1 * a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g + 200 * h
                                if sum == 200:
                                    print((a, b, c, d, e, f, g, h))
                                    plans.append((a, b, c, d, e, f, g, h))
                                elif sum > 200:
                                    break
print("Total=", len(plans))