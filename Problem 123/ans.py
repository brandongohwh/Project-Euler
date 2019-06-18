def prime(x):
    for i in range(2,x):
        if not x%i:
            return 0
    return 1
i=2
cnt=1
while True:
    z=prime(i)
    if z:
        minusnum=(i-1)**cnt
        plusnum=(i+1)**cnt
        tot=(minusnum%(i**2)+plusnum%(i**2))%(i**2)
        if tot>10000000000:
            print(cnt)
            break
        cnt+=1
    i+=1