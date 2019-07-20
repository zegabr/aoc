import sys
a=sys.stdin.read().split()
#print(a)
#f = open("i.txt",'r')
#a=f.read().split()
sum=0
for i in a:
    sum+=int(i)
print (sum)
