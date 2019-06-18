x1=1
x2=1
x3=x1+x2
cnt=3
while (len(str(x3))<1000):
    x1=x2
    x2=x3
    x3=x1+x2
    cnt+=1
print("First term with 1000 digits has index:",cnt)