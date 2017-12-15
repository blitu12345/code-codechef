t=input()
while(t):
	t-=1
	n,k,m=map(int,raw_input().split())
	arr=map(int,raw_input().split())
	i=0;count=0
	if(m!=1):
		while(i<=n-k):
			#print "iterate",i,n-k
			j=i;maxi=[0]
			while(j<=i+k-1):
				#print "innertrate",j,i+k-1
				if(arr[j]>maxi[0]):
					maxi=[]
					maxi.append(arr[j])
				elif(arr[j]==maxi[0]):
					maxi.append(arr[j])
				#	print ">>>",maxi,len(maxi)
					if(len(maxi)==m):
						count+=1
						try:
							if(arr[j+1]==arr[j]+1):
								arr[j-1]+=1
						except:
							arr[j]+=1
				j+=1
			#print maxi
			#print arr
			i+=1
		#print arr
		print count
	else:
		print -1