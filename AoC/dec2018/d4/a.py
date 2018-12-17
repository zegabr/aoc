from operator import attrgetter
import sys

t=sys.stdin.read().split('\n')

class line:
    month=0
    day=0
    hour=0
    minu=0
    op='n'
    ind=0
    def __init__( self,m, d,h,mi,i,opr):
        self.month=int(m)
        self.day=int(d)
        self.hour=int(h)
        self.minu=int(mi)
        self.ind=int(i)
        self.op=opr
    
    def p(self):
        print(self.month, self.day,self.hour,self.minu,self.op,self.ind)

obj=[]
for s in t:#this does not change t items
    s=s.replace("[1518-", "")
    s=s.replace("]","")
    s=s.replace("-"," ")
    s=s.replace(':',' ')
    s=s.replace('falls asleep','s 0')#sleep #index
    s=s.replace('wakes up', 'w 0')#wakes #index
    s=s.replace('Guard #', '')
    s=s.replace('begins shift', 'b')
    s=s.split()
    if(s[5]=='b'):
        s[4],s[5]=s[5],s[4]
    #print(s)
    s=line(s[0],s[1],s[2],s[3],s[5],s[4])
    #s.p()
    obj.append(s)#storing useful objects


##
t=obj
t=sorted(t,key=attrgetter('month','day','hour','minu'))

#updating indexes in order
curr=t[0].ind
for i in range(len(t)):
    if t[i].ind==0:
        t[i].ind=curr
    else:
        curr=t[i].ind
        
#till here everything is working properly
dic = dict()
for i in range(len(t)):
    #t[i].p()
    if t[i].op=='w':
        if t[i].ind not in dic:
            dic[t[i].ind]=t[i].minu-t[i-1].minu
        else:
            dic[t[i].ind]+=t[i].minu-t[i-1].minu
idans=0
maior=-1
for g,v in dic.items():
    if v>maior:
        idans=g
        maior=v
#print(idans)

mins=[0 for x in range(60)]
minuans=60
vezesnominuans=0
for i in range(len(t)):
    if t[i].op=='s' and t[i].ind==idans:
        for k in range(t[i].minu,t[i+1].minu):
            mins[k]+=1
            if mins[k]>vezesnominuans:
                minuans=k
                vezesnominuans=mins[k]
#print(minuans)
print(idans*minuans)