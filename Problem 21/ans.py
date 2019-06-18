def propfactor(x):
    l=[1]
    for i in range(2,x):
        if not x%i:
            l.append(i)
    return l

x=[z for z in range(2,10000)]
y=[sum(propfactor(w)) for w in range(2,10000)]

rm=1
while (rm==1):
    rm=0
    for i in range(len(x)-1,-1,-1):
        if y[i] not in x:
            y.pop(i)
            x.pop(i)
            rm=1
        elif x[i]==y[i]:
            y.pop(i)
            x.pop(i)
            rm=1
for i in range(len(x)-1,-1,-1):
    if y[i] not in x or y[x.index(y[i])]!=x[i]:
        y.pop(i)
        x.pop(i)
print("Sum of amicable numbers under 10000:",sum(x))