import numpy as np

a=np.zeros([21,21],dtype='int64')
a[:,0]=1
a[0,:]=1
for i in range(1,a.shape[0]):
    for j in range(1,a.shape[1]):
        a[i,j]=a[i-1,j]+a[i,j-1]
print("Number of routes:",a[a.shape[0]-1,a.shape[1]-1])