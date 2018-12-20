import sys
from string import ascii_lowercase
s=sys.stdin.read()
mini=len(s)

for c in ascii_lowercase:
    t=s.replace(c,"")
    t=t.replace(c.upper(),"")

    cont = 1 ## bool para continuar a operacao
    while(cont):
        cont=0
        i=0
        for i in range(len(t)-1):
            j=i+1
            if t[i].lower()==t[j].lower() and t[i]!=t[j]:
                t=t.replace(t[i]+t[j],"")
                cont=1
                break
 
    mini=min([mini,len(t)])
            
print(mini)
