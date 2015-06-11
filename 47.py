from sympy import factorint
nd={}
i=1
while True:
    nd[i]=len(factorint(i).keys())
    if nd[i]==4 and nd[i-1]==4 and nd[i-2]==4 and nd[i-3]==4:
        print(i-3)
        break
    i+=1