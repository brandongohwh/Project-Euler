L=[]
for p in range(0,1001):
    print(p)
    cnt=0
    for a in range(0,p+1):
        for b in range(0,a+1):
            for c in range(0,a+b+1):
                if (a*a==(b*b+c*c)) and a+b+c==p:
                    cnt+=1

    L.append(cnt)
print("Solutions maximised when p=%d"%L.index(max(L)))