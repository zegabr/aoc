import sys
t=sys.stdin.read().split('\n')
a=[[0 for x in range (1000)] for y in range(1000)]##2d array here


for line in t:
    line = line[1:]
    line = line.split()
    line[2]=line[2].split(',')
    line[2][1]=line[2][1][:-1]
    line[3]=line[3].split('x')
    index=line[0]
    sideoffset=int(line[2][0])
    topoffset=int(line[2][1])
    wid=int(line[3][0])
    hei=int(line[3][1])
    for i in range(topoffset,topoffset+hei):
        for j in range(sideoffset,sideoffset+wid):
            a[i][j]+=1
            
ans=0
for i in range(1000):
    for j in range(1000):
        ans+= (a[i][j]>1)
print(ans)