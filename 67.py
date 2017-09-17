import numpy
import time
st=time.monotonic()

arr_data = [line.split(" ") for line in open("triangle.txt")]
arr=numpy.zeros((len(arr_data),len(arr_data)),dtype=numpy.short)
for row in range(len(arr_data)):
    for item in range(len(arr_data[row])):
        arr[row][item] = int(arr_data[row][item])
print(arr)
for y in range(len(arr_data) - 2, -1, -1):
    for x in range(y + 1):
        if arr[y + 1][x] < arr[y + 1][x + 1]:
            arr[y][x] += arr[y + 1][x + 1]
        elif arr[y + 1][x] >= arr[y + 1][x + 1]:
            arr[y][x] += arr[y + 1][x]
print(arr[0][0])

et=time.monotonic()

print(et-st)