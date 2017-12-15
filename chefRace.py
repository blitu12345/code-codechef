t=input()
while(t>0):
	t-=1
	n=input()
	arr1=[1]*n
	sum1=0
	arr=map(int,raw_input().split())
	i=0
	while(i<n):
		if arr1[i]==1:
			sum1+=1
			arr1[i]=0
			j=i
			while(j<n):
				if arr1[j]==1 and arr[j]>arr[i]:
					arr1[j]=0
				j+=1
		i+=1
	print sum1