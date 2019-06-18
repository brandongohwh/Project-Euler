import math

x=str(math.factorial(100))
cnt=0
for i in x:
    cnt+=int(i)
print("Sum of digits in 100!:",cnt)