def palin(x):
    if str(x)[::-1]==str(x):
        return 1
    return 0

larg=0
for i in range(100,1000):
    for j in range(100,1000):
        if palin(i*j):
            if (i*j)>larg:
                larg=i*j
print("Largest palindrome from 2 3-digit numbers:", larg)