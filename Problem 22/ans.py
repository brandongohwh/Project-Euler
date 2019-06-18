import re
f=open('p022_names.txt','r')
x=re.split(',|\"',f.read())
for i in range(len(x)-1,-1,-1):
    if x[i]=='':
        x.pop(i)
x.sort()
y=[0]*len(x)
a={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
for i in range(len(x)):
    az=0
    for j in x[i]:
        for k in j:
            az+=a.get(k)
    y[i]=az*(i+1)
print("Total score:",sum(y))
