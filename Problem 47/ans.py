def primefactor(x):
    l=[]
    i=int(x)
    if x==1 or x==0:
        return 0
    while(i!=1):
        for j in range(2,i+1):
            if i%j==0:
                if j not in l:
                    l.append(j)
                i//=j
                break
    return len(l)

x=[]
for y in range(1,200000):
    x.append(primefactor(y))
for i in range(len(x)-4):
    if x[i:i+4]==[4]*4:
        print("First of 4 consecutive integers:",i+1)
        break