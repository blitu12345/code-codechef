t=input()
while(t>0):
	t-=1
	n=input()
	arr=map(int,raw_input().split())
	i=0
	sum1=0
	mini=arr[0]
	while(i<n):
		if(arr[i]<=mini):
			sum1+=1
			mini=arr[i]
		i+=1
	print sum1