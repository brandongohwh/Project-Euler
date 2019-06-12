f=open('number.txt','r')
x=f.read().split(',')
l=[int(y) for z in x for y in z if y.isdigit()]
maxprod=0
for i in range(len(l)-13):
    prod=1
    for j in range(13):
        prod*=l[i+j]
        if prod>maxprod:
            maxprod=prod
print("Max product of 13 adjacent numbers: %d"%maxprod)