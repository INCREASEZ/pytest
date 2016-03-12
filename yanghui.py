#-*- coding: utf-8 -*-
def triangles():
    pass
    l=[1]
    yield l
    while True:
       #l.append(0)
       #l.insert(0,0)
       #l=[l[x]+l[x+1] for x in range(len(l)-1)]
       l=[1]+[l[x]+l[x+1] for x in range(len(l)-1)]+[1]
       yield l
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break