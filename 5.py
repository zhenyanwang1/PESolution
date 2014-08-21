#TODO
num = 1
while True:
    ok = True
    for i in range(2, 21):
        if num % i != 0:
            ok = False
    if ok:
        print(num)
        break
    num += 1