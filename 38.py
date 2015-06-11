from itertools import cycle
def pan(s):
    if len(s)!=9:
        return False
    for d in "123456789":
        if not d in s:
            return False
    return True
def cp(i,n):
    ps=[]
    for mp in range(1,n+1):
        ps.append(str(i*mp))
    return "".join(ps)
for i in range(1,999999):
    cps=map(cp,cycle([i]),list(range(1,30)))
    for cp_ in cps:
        if pan(cp_):
            print(cp_)
            break