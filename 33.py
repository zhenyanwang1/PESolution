pu = 1
pd = 1
for u in range(10, 100):
    for d in range(10, 100):
        if str(u)[1] == str(d)[0] and str(d)[1] != "0" and u / d == int(str(u)[0]) / int(str(d)[1]) and u != d:
            print("{}/{}".format(u, d))
            pu *= u
            pd *= d
print("PRODUCT=", pu, "/", pd)