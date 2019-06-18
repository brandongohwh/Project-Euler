import re
f=open('number.txt','r')
x=list(map(int,re.split(',|\n',f.read())))
print(str(sum(x))[0:10])