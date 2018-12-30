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
for c in range(ord('A'),1+ord('F')):#############trocar F pra Z
    #print(c, g[c])
    if grau[c]==0:
        pq.append(c)

s=[]
steps=[]
step=[]
steps.append(pq)
#print(steps)
def timefor(num):
    return num - ord('A') + 1   ################colocar +60

while(len(pq)>0):
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
print(steps)
##working till here


total=len(ans)#total de tarefas a serem feitas

tempos=[0 for i in range(2)]##################3mudar pra 5 
tempo=0##tempo global
liberados=set()
liberados.add(steps[0][0])##prontos
feitos=set()##terminados
terminadoem={}##sendo feitos
while len(feitos)<total:
    tempo+=1
    for num in liberados:
        if num not in feitos and num not in terminadoem:
            for i in range(len(tempos)):
                if tempos[i]<tempo:
                    tempos[i]=tempo+num-1
                    terminadoem[num]=tempos[i]
                    break
    for k,v in terminadoem.items():
        if tempo==v:
            feitos.add(k)
            for step in steps:
                if step[0]==k:
                    for num in step[1]:
                        liberados.add(num)
                    break


    
    print("liberados = ",liberados)
    print("feitos = ",feitos)
    print("tempos = ", tempos)
    print("tempo = ",tempo)
    print()
    
print(tempo+1)