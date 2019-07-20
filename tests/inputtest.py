import sys
s="sad"
li = []
while(s!=""):
    s=sys.stdin.readline()
    if(s!='\n'):
        li.append(s)
for a in li:
    print (a)
