import sys

t=sys.stdin.read()#read everythint till eof and store as string
print(type(t))

print (t)
print()
t=t.split('\n')
print(t)
t2=[]
for line in t:
    line=line.strip()#removes trailing blank spaces
    if line!=' ' and line !='':
        t2.append(line)
#        print(line)
print()
print()
print(t2)
print()
print()
t=''
for line in t2:
    t=t+line+'\n'
print(t)