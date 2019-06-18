#Naive method, will take a few hours
mul=1
for i in range(1,1000000000000):
    while i%10==0:
        i//=10
    if len(str(i))>5:
        i=int(str(i)[-5:])
    mul*=i
    while mul%10==0:
        mul//=10
    if len(str(mul))>5:
        mul=int(str(mul)[-5:])
print("Last 5 digits before trailing zeros:",str(mul)[-5:])