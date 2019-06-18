hi=0
for a in range(1,1000000):
    b=0
    x=a
    while (x!=1):
        if(x%2):
            x=x*3+1
        else:
            x//=2
        b+=1
    if (hi<b):
        hi=b
        maxint=a
print("Starting number %d produces the longest chain of length %d"%(maxint,hi))