d=0
def prime(x):
    if x<0 or x==0 or x==1: #Must handle negative numbers
        return 0
    else:
        for i in range(2,x):
           if x%i ==0:
               return 0
        return 1

for a in range(-999,1000):
    for b in range(-1000,1001):
        c=0
        n=0
        while True:
            x=prime(n**2+a*n+b)
            if x==0:
                break
            c+=1
            n+=1
        if c>d:
            d=c
            l=(a,b)
            
print("Coefficients:",l,"yield",d,"primes, product=",l[0]*l[1])