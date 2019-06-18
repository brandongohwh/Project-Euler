import sympy

pr=list(sympy.sieve.primerange(2,1000000))
oddcomp=[2*x+1 for x in range(1,499999) if (2*x+1) not in list(sympy.sieve.primerange(2*x+1,2*x+2))]
sq=[2*x**2 for x in range(1000)]
for i in oddcomp:
    sqdup=sq[:]
    lgpr=pr[:sum([1 for j in pr if i>j])]
    sqdup=[i+x for x in sqdup for i in lgpr]
    if i not in sqdup:
        print(i,"fails Goldbach's conjecture")
        break