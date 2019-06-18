l=[]
cnt=1
peri=0
a=1
while(cnt!=(1001**2+1)):
    m=[]
    for i in range(a):
        m.append(cnt)
        cnt+=1
    peri+=1
    a=8*peri
    l.append(m)
h=[]
for i in range(len(l)-1,-1,-1):
    n=l[i]
    if -(i*2)==0:
        h.extend(n)
    else:
        for j in range(len(n)-1,-1,-(i*2)):
            h.append(n[j])
print("Sum of diagonals:",sum(h))