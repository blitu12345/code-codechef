t=input()
while(t>0):
	t-=1
	n=input()
	mark=[0]*100001;count=0;arr=[0]*(n+1)
	i=2;j=1
	while(i<n+1):
		arr[j]=i
		i+=2
		j+=1
	i=1
	while(j<n+1):
		arr[j]=i
		j+=1
		i+=2
	i=1
	while(i<n+1):
		#print "i",i
		if(mark[i]!=1):
			mark[i]=1
			index=i
			count+=1
			while(1):
				#print "index:",index
				j=arr[index]
				#print "j",j
				if(mark[j]==1):
					break
				mark[j]=1
				index=j
		i+=1
	i=0;j=1
	while(i<count):
		j*=26
		i+=1
	print j%1000000007