def prime(x):
    for i in range(2,x):
        if not x%i:
            return 0
    return 1

def divi(x):
    big=0
    div=2
    while(x!=1):
        if not x%div:
            if prime(x):
                if div>big:
                    big=div
            x//=div
            div=2
            continue
        div+=1
    return big

num=600851475143

print("Largest prime factor of %d is: %d"%(num,divi(num)))