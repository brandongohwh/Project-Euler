def prime(x):
    for i in range(2,a):
        if not x%i:
            return 0
    return 1

cnt=0
a=1
while cnt!=10001:
    a+=1
    if prime(a):
        cnt+=1
print("10001st prime number: %d"%a)