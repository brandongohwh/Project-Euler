pan2=[i*(3*i-1)/2 for i in range(1,5001)]

minnum=pan2[-1]
for i in range(len(pan2)-1):
    for j in range(i+1,len(pan2)):
        if pan2[j]-pan2[i] in pan2 and pan2[j]+pan2[i] in pan2 and pan2[j]-pan2[i]<minnum:
            minnum=pan2[j]-pan2[i]
print("D=%d"%minnum)