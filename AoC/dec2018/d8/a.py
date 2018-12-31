import sys
t=sys.stdin.read().split()
t=[int(x) for x in t]
#print(t,len(t))
tam=len(t)
tree=[]
node=[]
stack=[]
curr=0
qmeta=0
used=[0 for x in range(tam)]
for i in range(tam):
	if t[i]==0:
		stack.append(i)
		qmeta=t[i+1]
		used[i]=used[i+1]=1
		node=[i,[]]
		for x in range(i+2,i+2+qmeta):
			used[x]=1
			node[1].append(t[x])
		tree.append(node)
'''
print()
for k in tree:
	print(k)
exit()
'''
while len(stack)>0 :
	curr=stack.pop()-2
	if not used[curr] and not used[curr+2]:
		stack.append(curr)
	qmeta=t[curr+1]
	used[curr]=used[curr+1]=1
	node=[curr,[]]
	while qmeta>0 and curr<tam:
		if not used[curr]:
			qmeta-=1
			node[1].append(t[curr])
		curr+=1
	tree.append(node)


ans=0
print()
for k in tree:
	print(k)
	ans+=sum(k[1])
print(ans)
