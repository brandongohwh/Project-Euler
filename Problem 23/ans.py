a=[]
def prime(x):
    l=[]
    for i in range(1,x):
        if not x%i:
            l.append(i)
    return l

def abundant(l,x):
    if sum(l)>x:
        a.append(x)

for i in range(2,28123):
    abundant(prime(i),i)

x=[y for y in range(1,28123)]
for i in a:
    for j in a:
        if (i+j) in x:
            x.pop(x.index(i+j))
print("Non abundant sum:",sum(x))
