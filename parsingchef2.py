t = input()
while(t>0):
	t-=1
	n,m=map(int,raw_input().strip().split())
	a=[0]*m
	b=[0]*m
	s=[0]*n
	for i in range(m):
		a[i],b[i]=map(int,raw_input().split())
	s[a[-1]]=1;s[b[-1]]=1
	res=[]
	res.append(m-1)
	for i in range(m):
		if( s[a[i]]!=1 and s[b[i]]!=1 ):
			res.append(i)
			s[a[i]]=1
			s[b[i]]=1
	res=sorted(res)
	for i in res:
		print ("%d ")%(i)