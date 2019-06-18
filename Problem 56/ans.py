def sumlet(x):
    val=0
    a=str(x)
    for i in a:
        val+=int(i)
    return val

x=[0]*100**2
for i in range(100):
    for j in range(100):
        x[i*100+j]=sumlet(int(i**j))
print("Maximum digital sum:",max(x))