x1=1
x2=2
sumnum=0
x3=x1+x2

while(x1<=(4*10**6)):
    if not x1%2:
        sumnum+=x1
    x1=x2
    x2=x3
    x3=x1+x2

print("Sum of even numbered Fibonacci numbers <= 4 million:",sumnum)