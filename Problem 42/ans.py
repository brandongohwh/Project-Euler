import re

def lettonum(s):
    val=0
    for i in s:
        if i=='A':
            val+=1
        elif i=='B':
            val+=2
        elif i=='C':
            val+=3
        elif i=='D':
            val+=4
        elif i=='E':
            val+=5
        elif i=='F':
            val+=6
        elif i=='G':
            val+=7
        elif i=='H':
            val+=8
        elif i=='I':
            val+=9
        elif i=='J':
            val+=10
        elif i=='K':
            val+=11
        elif i=='L':
            val+=12
        elif i=='M':
            val+=13
        elif i=='N':
            val+=14
        elif i=='O':
            val+=15
        elif i=='P':
            val+=16
        elif i=='Q':
            val+=17
        elif i=='R':
            val+=18
        elif i=='S':
            val+=19
        elif i=='T':
            val+=20
        elif i=='U':
            val+=21
        elif i=='V':
            val+=22
        elif i=='W':
            val+=23
        elif i=='X':
            val+=24
        elif i=='Y':
            val+=25
        elif i=='Z':
            val+=26
    return val
a=[0.5*b*(b+1) for b in range(1,501)]
f=open('p042_words.txt','r')
b=re.split(',|\"',f.read())
x=[l for l in b if l!='']
y=[0]*len(x)
for i in range(len(x)):
    if lettonum(x[i]) in a:
        y[i]=1
print(sum(y),"are triangle words")
