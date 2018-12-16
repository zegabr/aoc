import sys
t=sys.stdin.read().split()


def differbyexactely2(s1,s2):
    dif=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            dif+=1
    return dif==1
    

ans=""
for s1 in t:
    for s2 in t:
        
        if differbyexactely2(s1,s2):
            for i in range(len(s1)):
                if(s1[i]==s2[i]):
                    ans+=s1[i]

            print(ans)
            exit()