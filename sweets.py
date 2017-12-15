t=input()
while(t):
	t-=1
	n ,p=map(int,raw_input().split())
	arrn=map(int,raw_input().split())
	i=0;sum1=0
	while(i<n):
		sum1+=arrn[i]
		i+=1
	s=sum1/p
	i=0
	while(i<n):
		if(arrn[i]<p):
			if(sum1-arrn[i])/p==s:
				s=-1
				break
		i+=1
	print s