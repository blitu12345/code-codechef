'''t=input()
n,k=map(int,raw_input().split())
arr2=[[0 for i in range(0)]for j in range(n+1)]
arr1=[0]*(n+1)
for i in range(2,n+1):
	print i,"i"
	if(arr1[i]==0):
		for j in range(i,n+1):
			if(j%i==0 and arr1[j]==0):
				print j
				arr1[j]=1
				arr2[i].append(j)'''

t=input()
for i in range(t):
	n,k=map(int,raw_input().split())
	if k>n/2 and k!=1:
		print -1
	elif k==1:
		print 1
	else:
		for i in range(1,k+1):
			print 2*i,
		print '\n'