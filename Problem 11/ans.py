import numpy as np

mat=np.loadtxt('grid.txt',dtype='int')

maxprod=-1

for i in range(mat.shape[0]):
    for j in range(mat.shape[1]-4):
        if np.product(mat[i,j:j+4])>maxprod:
            maxprod=np.product(mat[i,j:j+4])
        if np.product(mat[j:j+4,i])>maxprod:
            maxprod=np.product(mat[j:j+4,i])

for i in range(-mat.shape[0]+1,mat.shape[1]):
    a=np.diag(mat,i)
    if len(a)>=4:
        for j in range(len(a)-4):
            if np.prod(a[j:j+4])>maxprod:
                maxprod=np.prod(a[j:j+4])

mat=np.flipud(mat)
for i in range(-mat.shape[0]+1,mat.shape[1]):
    a=np.diag(mat,i)
    if len(a)>=4:
        for j in range(len(a)-4):
            if np.prod(a[j:j+4])>maxprod:
                maxprod=np.prod(a[j:j+4])
print("Greatest product:",maxprod)