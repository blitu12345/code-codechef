def Quick(arr):
	n=len(arr)
	if(n<=1):return arr
	i=0
	pivot=arr[i]
	i=0;Harr=[];Sarr=[];Earr=[]
	while(i<n):
		if( arr[i]>pivot):
			Harr.append(arr[i])
		elif(arr[i]<pivot):
			Sarr.append(arr[i])
		else:
			Earr.append(arr[i])
		i+=1
	return Quick(Sarr)+Earr+Quick(Harr)

arr=map(int,raw_input().split())
print Quick(arr)