# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 02:26:04 2019

@author: Brandon
"""

cnt=0
def ones(x):
    m=[4,3,3,5,4,4,3,5,5,4] #0->9
    return m[x]

def tens(x):
    if int (str(x)[0])==1:
        m=[3,6,6,8,8,7,7,9,8,8] #10->19
        return m[int(str(x)[1])]
    else:
        m=[6,6,5,5,5,7,6,6] #20->90 (tens only)
        if int(str(x)[1])!=0:
            return m[int(str(x)[0])-2]+ones(int(str(x)[1]))
        return m[int(str(x)[0])-2]

def hundreds(x):
    if int(str(x)[1:3])==0:
        return ones(int(str(x)[0]))+7
    elif int(str(x)[1:3])<10:
        return ones(int(str(x)[0]))+7+3+ones(int(str(x)[2]))
    else:
        return ones(int(str(x)[0]))+7+3+tens(int(str(x)[1:3]))
    
def thousands(x):
    if int(str(x)[1:])==0:
        return ones(int(str(x)[0]))+8
    elif int(str(x)[1:])<10:
        return ones(int(str(x)[0]))+8+3+ones(int(str(x)[3]))
    elif int(str(x)[1:])<100:
        return ones(int(str(x)[0]))+8+3+tens(int(str(x)[2:4]))
    else:
        return ones(int(str(x)[0]))+8+hundreds(int(str(x)[1:]))

def lencheck(x):
    if len(x)==1:
        return ones(dig)
    elif len(x)==2:
        return tens(dig)
    elif len(x)==3:
        return hundreds(dig)
    else:
        return thousands(dig)

for dig in range(1,1001):
    x=str(dig)
    cnt+=lencheck(x)
print("Number of letters from 1 to 1000:",cnt)