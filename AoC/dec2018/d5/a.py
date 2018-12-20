import sys
s=sys.stdin.read()
cont = 1 ## bool para continuar a operacao



while(cont):
    cont=0
    i=0
    for i in range(len(s)-1):
        j=i+1
        if s[i].lower()==s[j].lower() and s[i]!=s[j]:
            s=s.replace(s[i]+s[j],"")
            cont=1
            break
            
            
print(len(s))
