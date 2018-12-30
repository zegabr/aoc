##constants
qworkers=2  #2 for base case and 5 for bigger case
alphabetlimit='F' # F for base case and Z for biggercase
secondoffset=0 #0 for base case and 60 for biggercase
###


import sys
inp = sys.stdin.read().split('\n')
g=[set() for x in range(10+ord('Z'))]##dicionario de sets, grafo
g2=[set() for x in range(10+ord('Z'))]##grafo invertido
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
    g2[ord(b)].add(ord(a))
    grau[ord(b)]+=1


ans=""
pq=[]#heap.. ish
for c in range(ord('A'),1+ord(alphabetlimit)):
    #print(c, g[c])
    if grau[c]==0:
        pq.append(c)

s=[]
steps=[]
step=[]
steps.append(pq)
#print(steps)
def timefor(num):
    return num - ord('A') + 1 + secondoffset

while len(pq)>0:
    pq.sort()
    pq.reverse()
    parent=pq[-1]
    step=[timefor(parent),[]]    
    #print(pq)
    pq.pop()#min heap top
    for child in g[parent]:
        grau[child]-=1
        if visited[child]==0:
            if grau[child]==0:
                pq.append(child)
                
                step[1].append(timefor(child))

    steps.append(step)
    step=[]
    ans+=chr(parent)
    visited[parent]

steps=[steps[x] for x in range(len(steps)) if steps[x]!=[]]
print(ans) 
#print(steps)
tempos=[0 for i in range(qworkers)]
tempo=0
liberados=set()
feitos=set()
terminaranotempo=dict()
maxtime=sum([timefor(num) for num in range(ord('A'),ord(alphabetlimit)+1)])
print(maxtime)
liberados.add(steps[0][0])
s=dict()
for step in steps:
    s[step[0]]=step[1]
steps=s
del s
print(steps)

precedentes=dict()
for a in range(len(g2)):
    if g2[a]!=set():
        precedentes[timefor(a)]={timefor(b) for b in g2[a]}

##working till here
def libera(num):
    for precedente in precedentes[num]:
        if precedente not in feitos:
            return 0
    return 1

while tempo<=maxtime and len(feitos)<len(ans):
    

    tempo+=1
    for num in sorted(list(liberados)):
        if num not in terminaranotempo.keys() and num not in feitos:
            for i in range(len(tempos)):
                if tempo>=tempos[i]:
                    tempos[i]=tempo+num-1
                    terminaranotempo[num]=tempos[i]
                    break
    

    for k,v in terminaranotempo.items():
        if tempo>=v:
            feitos.add(k)
            
            for num in steps[k]:
                if libera(num):
                    liberados.add(num)
    

    print("feitos: ", [chr(x+ord('A')-1-secondoffset) for x in feitos])
    print("prontos: ",[chr(x+ord('A')-1-secondoffset) for x in liberados])
    print("em progresso: ", terminaranotempo)
    print("tempos: ", tempos)
    print("tempo total: ", tempo, "s")
    print()


print(tempo)
