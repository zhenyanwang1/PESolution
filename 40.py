from functools import reduce
from operator import mul
s="".join([str(i) for i in range(1,1000000+1)])
ret=[int(s) for s in [s[1-1],s[10-1],s[100-1],s[1000-1],s[10000-1],s[100000-1],s[1000000-1]]]
print(reduce(mul,ret))