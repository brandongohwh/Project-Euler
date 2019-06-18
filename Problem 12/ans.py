def primelist(x):
    l=[1]
    for i in range(2,x+1):
        if not x%i:
            l.append(i)
    return len(l)
i=1
diff=1
while True:
    diff+=1
    if primelist(i)>500:
        break
    i+=diff
print(i,"has over 500 divisors")