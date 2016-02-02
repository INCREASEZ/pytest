#-*- coding:utf-8 -*-

#2-3
print(5//2)
print(3**2)
ind2=input("number:")
print("%d" % int(ind2))

#2-5
i=0
while(i<11):
    i=i+1
    print(i)

for j in range(11):
    print(j)

#2-6
ind3=int(input("num:"))
if ind3>0:
    print(">0")
elif ind3<0:
    print("<0")
else:
    print("=0")

#2-7
ind=input("input:")
k=0
while k<len(ind):
    print(ind[k],end="")
    k=k+1
print(end='\n')
for o in ind:
    print(o,end='')
print(end='\n')

#2-9
ind4=range(5)
ind5=(2,2,3,4,5)
f=lambda x:x[0]+x[1]+x[2]+x[3]+x[4]
print(f(ind4)/5.0)
print(f(ind5)/5)