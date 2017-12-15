def func(n):
	i = 1
 	sum2 = 0
   	while( i<=n ):
   		if( n%i==0 ):
   			sum2=sum2+i
   		i=i+2
   	return sum2
     
t = input()
while(t>0):
   	i,s = map(int,raw_input().split())
   	sum1 = 0
   	while( i<=s ):
   	    sum1 = sum1 + func(i)
   	    i = i + 1
   	print sum1
   	t = t -1