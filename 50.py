from sympy import primerange
ps=list(primerange(1, 1000000))
print(len(ps))
for pos in range(len(ps)):
    for length in range(20,len(ps)):
        if sum(ps[pos:pos+length]) in ps:
            print(sum(ps[pos:pos+length]))