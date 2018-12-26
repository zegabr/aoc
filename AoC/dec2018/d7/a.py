import sys
inp = sys.stdin.read().split('\n')
g=[set() for x in range(10+ord('Z'))]##dicionario de sets, grafo
grau=[0 for x in range(10+ord('Z'))]## grau de entrada dos vertices
visited=grau#elementos visitados
for i in range(len(inp)):
    inp[i]=inp[i].replace("Step ","")
    inp[i]=inp[i].replace(" must be finished before step","")
    inp[i]=inp[i].replace(" can begin.","")
    inp[i]=inp[i].split()
    a,b=inp[i]
    #print(ord(a),ord(b))
    g[ord(a)].add(ord(b))
    grau[ord(b)]+=1
    
ans=""
pq=[]#heap.. ish
for c in range(ord('A'),1+ord('Z')):
    #print(c, g[c])
    if grau[c]==0:
        pq.append(c)

    
while(len(pq)>0):
    pq.sort()
    pq.reverse()
    parent=pq[-1]
    
    #print(pq)
    pq.pop()#min heap top

    for child in g[parent]:
        grau[child]-=1
        if visited[child]==0:
            if grau[child]==0:
                pq.append(child)

    ans+=chr(parent)
    visited[parent]

print(ans)    