t=input()
c=t
count=[[0 for i in range(t)] for j in range(26)];arr=[[]for i in range(t)]
while(t>0):
	arr[t-1]=list(raw_input())
	t-=1
j=0
##print arr
while(j<c):
	i=0;n=len(arr[j])
	while(i<n):
		iter1=(ord(arr[j][i])-19)%26
		count[iter1][j]+=1
		i+=1
	j+=1
#print count
i=0;t=c;c=''
while(i<26):
	j=t;min1=99999999
	while(j>=0):
		j-=1
		if(count[i][j]<min1):
			min1=count[i][j]
	j=0
	while(j<min1):
		c+=chr(97+i)
		j+=1
	i+=1
if(len(c)==0):
	print "no such string"
else:
	print c







'''
n=input()
a=[1000]*26
for i in range(n):
    b=[0]*26
    s=raw_input()
    for i in range(0,len(s)):
        b[ord(s[i])-97]+=1
    for i in range(0,26):
        a[i]=min(a[i],b[i])
s=""
for i in range(0,26):
    if a[i]!=1000:
        x=a[i]
        s=s+str(unichr(i+97))*x
if len(s)>0:
    print s
else:
    print "no such string"
    '''