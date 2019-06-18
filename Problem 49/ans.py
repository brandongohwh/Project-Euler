import sympy
import itertools

x=list(sympy.sieve.primerange(1000,10000))
for i in range((len(x)-2)):
    t=list(itertools.permutations(str(x[i]),len(str(x[i]))))
    tc=[''.join(y) for y in t]
    for j in range(i+1,(len(x)-1)):
        diff1=x[j]-x[i]
        for k in range(j+1,(len(x))):
            diff2=x[k]-x[j]
            if diff1==diff2:
                if str(x[k]) in tc and str(x[j]) in tc:
                    print("Concatenation of: (%d, %d, %d)\n"% (x[i],x[j],x[k]))
