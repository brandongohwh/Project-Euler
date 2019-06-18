import sympy

l=[]
x=list(sympy.sieve.primerange(2,7072))
z=list(sympy.sieve.primerange(2,369))
aa=list(sympy.sieve.primerange(2,85))
for i in x:
    for j in z:
        for k in aa:
            su=(i**2+j**3+k**4)
            if su<50000000:
                l.append(su)
            else:
                break
print("Numbers below 50 million:",len(set(l)))