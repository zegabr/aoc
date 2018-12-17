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
minutomaisdormido=-1
freqminutomaisodrmido=-1
indans=-1

for i in range(len(t)):
    #t[i].p()
    if t[i].op=='s':
        if t[i].ind not in dic:
            dic[t[i].ind]=[0 for x in range(60)]
        for j in range(t[i].minu,t[i+1].minu):
            dic[t[i].ind][j]+=1
            if(dic[t[i].ind][j] > freqminutomaisodrmido):
                freqminutomaisodrmido=dic[t[i].ind][j]
                minutomaisdormido=j
                indans=t[i].ind

print(indans*minutomaisdormido)