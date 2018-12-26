import sys
from operator import itemgetter
t=sys.stdin.read().split('\n')
n=360
a=[['.' for y in range(n)] for x in range(n)]
for i in range(len(t)):
    t[i]=t[i].split(", ")
    t[i][0]=int(t[i][0])
    t[i][1]=int(t[i][1])
    a[t[i][0]][t[i][1]]=i

ans=0
for i in range(n):
    for j in range(n):
        sum=0
        for k in range(len(t)):
            dx,dy=t[k][0],t[k][1]
            sum+=abs(dx-i)+abs(dy-j)
        if sum<10000 : 
            ans+=1
print(ans)