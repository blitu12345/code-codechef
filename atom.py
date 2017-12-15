t=input()
while(t>0):
	t-=1
	n,m=map(int,raw_input().split())
	arr=[0]*n;s=[[[] for i in range(0)]for j in range(m)]
	i=0;j=0;k=0
	while(i<m):
		arr1=map(int,raw_input().split())
		j=0
		while(j<arr1[0]):
			arr[arr1[1+j]]+=1
			s[i].append(arr1[j+1])
			j+=1
		i+=1
	#print 
	#print "arr1",arr
	#print s
	#print 

	i=0;sum1=0
	while(i<n):
		if(arr[i]>1):
			sum1+=1
			arr[i]=0
		i+=1

	#print "arr2",arr

	sum2=[0]*m;i=0;j=0

	while(i<n):
		if(arr[i]==1):
			j=0
			while(j<m):
				k=0
				while(k<len(s[j])):
					if(i==s[j][k]):
						sum2[j]=1
					k+=1
				j+=1
		i+=1

	print sum1+sum(sum2)
	print 