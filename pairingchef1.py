


t = input()
while(t>0):
	t-=1
	n,m=map(int,raw_input().split())
	a=[0]*m
	b=[0]*m
	for i in range(m):
		a[i],b[i]=map(int,raw_input().split())
	A=[];A.append(m-1)
	count=1
	#print "A"
	#print A
	while(count!=0):
		count=0
		for i in range(m):
			#print "i"
			#print i
			if(count==1):
				break
			for j in A:
				#print "i,j"
				#print ("%d %d")%(i,j)
				if( i!=j and a[i]!=a[j] and b[i]!=b[j] and a[i]!=b[j] and b[i]!=a[j] ):
					#print "for=for-if"
					count+=1
					A.append(i)
					break
	for j in A:
		print j,
