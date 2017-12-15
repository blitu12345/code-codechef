t=input()
while(t):
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	count=[0]*10001;max1=[]
	i=0;p=False
	while(i<n):
		count[arr[i]]+=1
		if(count[arr[i]]==2):
			max1.append(arr[i])
		if(count[arr[i]]>=4):
			p=True
		i+=1
	#print "max1"
	#print max1
	if(p or len(max1)>=2):
		arr=[]
		max1=sorted(max1,reverse=True)
		arr.append(max1[0])
		#print "arr"
		#print arr
		if(count[arr[0]]>=4):
			print arr[0]**2
		else:
			arr.append(max1[1])
			print arr[0]*arr[1]
	else:
		print -1