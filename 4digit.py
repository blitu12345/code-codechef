for i in range(input()):
	m=input()
	n=len(str(m))
	count=0
	while(n>0):
		if(m%10==4):
			count+=1
		m=m/10
		n-=1
	print count