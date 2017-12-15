t=input()
arr=map(int,raw_input().split())
p=input()
suma=0
find=0
for i in range(t):
	find=p-arr[i]
	for j in range(i+1,t):
		if find==arr[j]:
			suma+=1
print suma