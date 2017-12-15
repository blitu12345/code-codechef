for i in range(int(raw_input())):
	for j in range(int(raw_input())):
		k,n,q=map(int,raw_input().split())
		a=[k]*n
		m=n
		p=0
		r=0
		while(p<m):
			if(n%2!=0):
				a[p]=0
				r+=1
			n-=1
			p+=1
		if(q==k):
			print len(a)-r
		else:
			print r