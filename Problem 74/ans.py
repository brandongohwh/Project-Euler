import math

def factloop(x):
    l=[int(x)]
    while True:
        c=0
        for i in x:
            c+=math.factorial(int(i)) 
        if (c in l):
            return l
        x=str(c)
        l.append(int(x))

cnt=0
for i in range(1,10**6+1):
    x=str(i)
    a=factloop(x)
    if type(a)==type([1]):
        if len(a)==60:
            cnt+=1
print("Number of chains with 60 non-repeating terms:",cnt)