import sympy

leng=0
num=0
x=list(sympy.sieve.primerange(2,1000000))
for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if (sum(x[i:j+1])>1000000):
            break
        if (sum(x[i:j+1]) in x) and (j-i)>=leng and sum(x[i:j+1])>num:
            leng=j-i
            num=sum(x[i:j+1])
print("Largest prime under 1 million:",num)