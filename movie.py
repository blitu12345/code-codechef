t = input()

while(t>0):
	n = input()
	l = map(int,raw_input().split())
	r = map(int, raw_input().split())
	m = 0
	maxi = 0
	max2 = 0
	ra = 0
	while(m<n):
		l[m]=l[m]*r[m]
		if( maxi<=l[m] ):
		    maxi=l[m]
		    if( max2<=r[m] ):
		        max2=r[m]
		m = m +1
	'''print "@@@"
	print l
	print r
	print maxi
	print max2'''
	p=1
	for i in range(n):
	    if( l[i]==maxi and r[i]==max2 ):
	        print p
        p = p + 1
	t = t - 1