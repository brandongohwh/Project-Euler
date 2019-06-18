cnt=0
for i in range(1,10000):
    l=i
    palin=0
    for j in range(49):
        lrev=int(str(l)[::-1])
        l+=lrev
        if str(l)==str(l)[::-1]:
            palin=1
            break
    if palin==0:
        cnt+=1
print("%d Lychrel numbers below 10000"%cnt)