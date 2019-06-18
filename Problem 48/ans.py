tot=0
for i in range(1,1001):
    tot+=(i**i)
print("Last 10 digits=",str(tot)[-10:])