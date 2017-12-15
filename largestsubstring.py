def freq(arr):
	#print "enter-func"
	#print arr
	n=len(arr)
	count=[0]*26;index=0;p=True
	while(index<n):
		#print "while"
		i=(ord(arr[index])-96)%26
		#print "i"
		count[i]+=1
		if(count[i]>1):
			p=False
			break
		index+=1
	return p,n


t=input()
while(t>0):
	#print "while-1"
	t-=1
	arr=list(raw_input())
	i=0;n=len(arr);max1=0
	while(i<n):
		#print "i,j"
		j=i+1
		while(j<n):
			#print ("%d-%d")%(i,j)
			p,count=freq(arr[i:j+1])
			'''print "count"
			print count
			print p'''
			if(p):
				j+=1
				if(max1<count):
					max1=count
			else:
				break
		i+=1
	#print "max1"
	print max1