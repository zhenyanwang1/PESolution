def calc(name):
    total=0
    for chr in name:
        total+=ord(chr)-64
    return total
f=open("names.txt")
names=[eval(name) for name in f.read().split(",")]
names.sort()
total=0
for i in range(len(names)):
    total+=calc(names[i])*(i+1)
print(total)