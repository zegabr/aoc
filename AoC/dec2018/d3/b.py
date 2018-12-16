import sys
t=sys.stdin.read().split('\n')
a=[[0 for x in range (1000)] for y in range(1000)]##2d array here

overlaps = set()
indexes = set()
for line in t:
    line = line[1:]
    line = line.split()
    line[2]=line[2].split(',')
    line[2][1]=line[2][1][:-1]
    line[3]=line[3].split('x')
    index=line[0]
    indexes.add(index)
    sideoffset=int(line[2][0])
    topoffset=int(line[2][1])
    wid=int(line[3][0])
    hei=int(line[3][1])
    for i in range(topoffset,topoffset+hei):
        for j in range(sideoffset,sideoffset+wid):
            if a[i][j]==0 :
                a[i][j]=index
            else:
                overlaps.add(index)
                overlaps.add(a[i][j])
            
for id in indexes:
    if id not in overlaps:
        print(id)
        exit()