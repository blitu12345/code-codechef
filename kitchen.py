
t = input()
while(t>0):
	t-=1
	n = input()
	allotment = map(int,raw_input().split())
	provided = map(int,raw_input().split())
	allotment[1:] = [ allotment[i]-allotment[i-1] for i in range(1,n) ]
	count = 0
	for i in range(n):
		if( allotment[i] >= provided[i] ): count+=1
	print count