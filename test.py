#-*- coding:utf-8 -*-
ind=input("input:")
k=0
while k<len(ind):
    print(ind[k],end="")
    k=k+1
print(end='\n')
for o in ind:
    print(o,end='')
print(end='\n')

print(5//2)
print(3**2)
ind2=input("number:")
print("%d" % int(ind2))
i=0
while(i<11):
    i=i+1
    print(i)

for j in range(11):
    print(j)

ind3=int(input("num:"))
if ind3>0:
    print(">0")
elif ind3<0:
    print("<0")
else:
    print("=0")