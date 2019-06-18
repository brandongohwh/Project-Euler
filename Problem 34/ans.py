import math
a=[math.factorial(x) for x in range(10)]

def factloop(x):
    su=0
    for i in str(x):
        su+=a[int(i)]
    return su

cnt=0
l=[]
for i in range(10,10000000):
    if i==factloop(i):
        l.append(i)
print("Sum of digit factorials: %d"%sum(l))