sum=0
for i in range(1,1000000+1):
    bs=bin(i)[2:]
    ds=str(i)
    if ds==ds[::-1] and bs==bs[::-1]:
        print(bs,ds)
        sum+=i
print("SUM=",sum)