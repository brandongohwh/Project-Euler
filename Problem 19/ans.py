x=['tue','wed','thur','fri','sat','sun','mon']
yr=[x for x in range(1901,2001)]
mnth=[31,28,31,30,31,30,31,31,30,31,30,31]
leap=[31,29,31,30,31,30,31,31,30,31,30,31]

def lpyr(x):
    if x%400==0:
        return 1
    elif x%100==0:
        return 0
    elif x%4==0:
        return 1
    return 0

l=[]
num=0
for i in yr:
    if lpyr(i):
        for j in range(len(leap)):
            m=[]
            for k in range(leap[j]):
                m.append(x[num%7])
                num+=1
            l.append(m)
    else:
        for j in range(len(mnth)):
            m=[]
            for k in range(mnth[j]):
                m.append(x[num%7])
                num+=1
            l.append(m)
cnt=0
for i in range(len(l)):
    if l[i][0]=='sun':
        cnt+=1
print("Number of Sundays in 20th century:",cnt)