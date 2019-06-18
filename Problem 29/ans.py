l=[]
for i in range(2,101):
    for j in range(2,101):
        l.append(i**j)
print("Number of distinct terms:",len(set(l)))