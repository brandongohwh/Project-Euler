L=[]
f=open('triangle.txt')
for line in f:
    L.append(list(map(int,line.split(' '))))
    
for i in range(1,len(L)):
    l1=L[i][0:-1]
    r1=L[i][1:]
    for j in range(len(L[i-1])):
        l1[j]+=L[i-1][j]
        r1[j]+=L[i-1][j]
    for j in range(len(L[i])):
        if j==0:
            L[i][j]=l1[0]
        elif j==len(L[i])-1:
            L[i][j]=r1[-1]
        else:
            L[i][j]=max(l1[j],r1[j-1])
print("Maximum:",max(L[len(L)-1]))