
su=0
for a in range(3,1001):
    l=[0]*10000
    for n in range(10000):
        l[n]=((((a-1)**n)%(a**2))+(((a+1)**n)%(a**2)))%(a**2)
    su+=max(l)
print("Sum rmax:",su)