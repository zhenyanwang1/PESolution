import numpy

n = 20
n += 1  # nodes=cells+1
arr = numpy.zeros((n, n), dtype=numpy.int64)
for i in range(n):
    arr[0, i] = 1
    arr[i, 0] = 1
for x in range(n):
    for y in range(n):
        if arr[x, y] == 0:
            arr[x, y] = arr[x - 1, y] + arr[x, y - 1]
