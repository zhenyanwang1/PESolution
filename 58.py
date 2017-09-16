from itertools import count

# from numpy import zeros, int32
from sympy import isprime


def roundup(x):
    if x % 2 != 0:
        return x // 2 + 1
    else:
        return x // 2


def cmds(n):
    mapping = {"R": "U", "U": "L", "L": "D", "D": "R"}
    direction = "R"
    step = 1
    status = 0
    while step <= n - 1:
        yield direction, step
        direction = mapping[direction]
        if status == 0:
            status = 1
        elif status == 1:
            status = 0
            step += 1


# def gen_spiral(n):
#     if n % 2 == 0:
#         raise Exception('n illegal')
#     arr = zeros((n, n), dtype=int32)
#     center = int((n - 1) / 2)
#     r, c = center, center
#     arr[r, c] = 1
#     pos = 2
#     for cmd in list(cmds(n)) + [("R", n - 1)]:
#         if cmd[0] == "R":
#             for x in range(cmd[1]):
#                 c += 1
#                 arr[r, c] = pos
#                 pos += 1
#         elif cmd[0] == "L":
#             for x in range(cmd[1]):
#                 c -= 1
#                 arr[r, c] = pos
#                 pos += 1
#         elif cmd[0] == "U":
#             for x in range(cmd[1]):
#                 r -= 1
#                 arr[r, c] = pos
#                 pos += 1
#         elif cmd[0] == "D":
#             for x in range(cmd[1]):
#                 r += 1
#                 arr[r, c] = pos
#                 pos += 1
#     return arr


def gen_diags():
    yield 1
    count = 1
    num = 3
    while True:
        yield num
        num += (count // 4 + 1) * 2
        count += 1

count=0
prime_count=0
for diag in gen_diags():
    print(diag)
    count+=1
    if isprime(diag) and diag!=1:
        prime_count+=1
    if prime_count/count<0.1 and count!=1:
        print((count-1)//4*2+1)
        break

"""
R1
U1
L2
D2
R3
U3
L4
D4

1 3 5 7 9  =2
13 17 21 25  =4
31 37 43 49  =6
"""

# 24001
