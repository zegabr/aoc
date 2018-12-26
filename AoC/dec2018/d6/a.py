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

for i in range(n):
    for j in range(n):
        if(a[i][j]=='.'):
            
            dis=dict()
            for k in range(len(t)):
                dx,dy=t[k][0],t[k][1]
                dis[k]=abs(dx-i)+abs(dy-j)
            
            dis=sorted(dis.items(),key=itemgetter(1))
            if(dis[0][1]!=dis[1][1]):
                a[i][j]=dis[0][0]
m={}
maxsize=-8967674231
ans=-1
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            m[a[i][j]]=-8967674231
        else:
            if a[i][j] not in m:
                m[a[i][j]]=1
            else:
                m[a[i][j]]+=1
                if m[a[i][j]]>maxsize:
                    maxsize=m[a[i][j]]
                    ans=a[i][j]
print(maxsize)           
        
    