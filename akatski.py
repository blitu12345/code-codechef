n=input()
t=0;a=[[]]*n
while(t<n):
	a[t]=map(int,raw_input().split())
	t+=1
t=0;l=[[]]*n
while(t<n):
	l[t]=map(int,raw_input().split())
	t+=1
a=sorted(a)
l=sorted(l)
t=0;count=0
while(t<n):
	s=abs(a[t][0]-l[t][0])+abs(a[t][1]-l[t][1])
	#print "t,index",t,index
	#print "ans",ans
	count+=s
	t+=1
print count