import sympy

a=list(sympy.sieve.primerange(2,1000000))
b=list(sympy.sieve.primerange(9,1000000))
l=[]
for c in b:
    d=str(c)
    e=str(c)
    for i in range(len(d)-1):
        d=d[1:]
        e=e[:-1]
        if int(d) not in a:
            break
        if int(e) not in a:
            break
        if len(d)==1:
            l.append(c)
print(len(l))