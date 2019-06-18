l=[]
cnt=0
for i in range(10,999999):
    if i==sum([int(j)**5 for j in str(i)]):
        l.append(i)
print("Sum of numbers equal to digit of 5th power: %d"%sum(l))