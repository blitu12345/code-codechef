for _ in range(input()):
	s=raw_input()
	n=input()
	t,st=0,0
	for i in s:
		if i=='T':
			t+=2
			#print t
		else:
			st+=1
	sum=t+st
	#print sum
	temp=12*n
	j,i,c=temp,1,0
	while i<=temp:
		j=temp-i
		while j:
			j-=sum
			if j>=0:
				c+=1
			
			if j-sum<0:
				break
		i+=1
		if temp-i<sum:
			break
	print c