def cutter(a,b,A,B):
	#print "cutter"
	#print a
	#print b
	#print A
	#print B
	n=len(a)
	if(n==1):
		A.append(a[0])
		B.append(b[0])
	elif(n>1):
		remA=[]
		A.append(a[-1])
		B.append(b[-1])
		for i in range(n):
			if(a[i]==a[-1] or b[i]==b[-1] or a[i]==b[-1] or b[i]==a[-1]):
				remA.append(a[i])
				remA.append(b[i])
		for i in range(len(remA)):
			if(i%2==0):
				a.remove(remA[i])
			else:
				b.remove(remA[i])
		cutter(a[:],b[:],A,B)

t = input()
while(t>0):
	t-=1
	n,m=map(int,raw_input().split())
	a=[0]*m
	b=[0]*m
	for i in range(m):
		a[i],b[i]=map(int,raw_input().split())
	A=[];B=[]
	cutter(a[:],b[:],A,B)
	n = len(A)
	for i in range(m):
		for j in range(n):
			if(a[i]==A[j]and b[i]==B[j]):
				print i,