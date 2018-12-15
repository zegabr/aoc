#import sys
#a=sys.stdin.read().split()
#print(a)
f = open("i.txt",'r')
a=f.read().split()
sum=0
t={0}#set only with value 0
while(True):
    for x in a:
        sum+=int(x)
        if(sum in t):
            print(sum)    
            exit()
        else:
            t.add(sum)
