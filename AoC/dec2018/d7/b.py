##constants
qworkers=5  #2 for base case and 5 for bigger case
alphabetlimit='Z' # F for base case and Z for biggercase
secondoffset=60 #0 for base case and 60 for biggercase
###
import sys
inp = sys.stdin.read().split('\n')
g=[set() for x in range(10+ord('Z'))]##dicionario de sets, grafo
g2=[set() for x in range(10+ord('Z'))]##grafo invertido

for i in range(len(inp)):
    inp[i]=inp[i].replace("Step ","")
    inp[i]=inp[i].replace(" must be finished before step","")
    inp[i]=inp[i].replace(" can begin.","")
    inp[i]=inp[i].split()
    a,b=inp[i]
    g[ord(a)].add(ord(b))
    g2[ord(b)].add(ord(a))
    

###
def timefor(num):
    return num - ord('A') + 1 + secondoffset
###

tempos=[0 for i in range(qworkers)]
tempo=0
liberados=set()
feitos=set()
terminaranotempo=dict()

precedentes=dict()
graph=dict()

###
def libera(num):
    for precedente in precedentes[num]:
        if precedente not in feitos:
            return 0
    return 1
###

for a in range(len(g2)):
    if g2[a]!=set():
        precedentes[timefor(a)]={timefor(b) for b in g2[a]}
for a in range (len(g)):
    if g[a]!=set():
        graph[timefor(a)]={timefor(b) for b in g[a]}
primeiros=[]
for i in range(timefor(ord('A')), timefor(ord(alphabetlimit)+1)):
    if i not in precedentes.keys():
        primeiros.append(i)
liberados={x for x in primeiros}

while len(feitos)<ord(alphabetlimit)-ord('A')+1:
    for num in sorted(list(liberados)):
        if num not in terminaranotempo.keys() and num not in feitos:
            for i in range(len(tempos)):
                if tempo>tempos[i]:
                    tempos[i]=tempo+num-1
                    terminaranotempo[num]=tempos[i]
                    break
    

    for k,v in terminaranotempo.items():
        if tempo>=v:
            feitos.add(k)
            if k in graph.keys():
                for num in graph[k]:
                    if libera(num):
                        liberados.add(num)
    tempo+=1
    
'''
    print("feitos: ", [chr(x+ord('A')-1-secondoffset) for x in feitos])
    print("prontos: ",[chr(x+ord('A')-1-secondoffset) for x in liberados])
    print("em progresso: ", terminaranotempo)
    print("tempos: ", tempos)
    print("tempo total: ", tempo, "s")
    print()
'''

print(tempo-1)
