t = input()
while(t>0):
	t-=1
	m = map(int,list(raw_input()))
	n = len(m)
	a=[0]*10
	if( n%2==0 ):
		for i in range(n/2):
			a[m[i]]+=1
			a[m[n-1-i]]+=1
	else:
		for i in range((n-1)/2):
			a[m[i]]+=1
			a[m[n-i-1]]+=1
	n=0
	for i in range(10):
		if( a[i]%2!=0 ):
			print "losses"
			n=1
			break
	if( n!=1 ):
		print "wins"