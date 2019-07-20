import sys
t=sys.stdin.read().split()

ans2=ans3=0
m={}

for s in t:
    bol2=bol3=0
    m.clear()
    
    for c in s:
        if c not in m:
            m[c]=1
        else:
            m[c]+=1
    
    for v in m.values():
        if v==2:
            bol2=1
        elif v==3:
            bol3=1
    
    ans2+=bol2
    ans3+=bol3
print (ans2*ans3)
