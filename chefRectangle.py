t=int(raw_input())
while(t>0):
	t-=1
	n,m,k=map(int,raw_input().split())
	r=n+m-3
	tt=n*m-2
	if tt<=0 or r<=0:
		print 0
	else:
		c=tt/r
		if c==1:
			print 1*k
		else:
			print (k/2 + k%2)