def payed(amount,mark,arr,n):
	#print "fun"
	#print "amount",amount
	if(amount==0):
	#	print "if-1"
		return 1
	i=0;count=0
	while(i<n):
		if(arr[i]<=amount and mark[i]!=1):
	#		print "minus",arr[i],"from",amount
			mark[i]=1
			if( payed(amount-arr[i],mark[:],arr,n ) ):
	#			print "if-2"
				return 1
		i+=1
	#print "ducki"
	return 0

t=input()
while(t>0):
	t-=1
	n,m=map(int,raw_input().split())
	i=0;arr=[0]*n;mark=[0]*n
	while(i<n):
		arr[i]=input()
		i+=1
	if(payed(m,mark,arr,n)):
		print "Yes"
	else:
		print "No"




#include<bits/stdc++.h>
 
using namespace std;
 
bool isSubset(int arr[],int sum,int n)
{
    if(sum==0)
        return true;
    if(n==0 && sum>0)
        return false;
    if(arr[n-1]>sum)
        return isSubset(arr,sum,n-1);#no need to tset this one as it is already inclued in the below.
 
    return isSubset(arr,sum,n-1)||isSubset(arr,sum-arr[n-1],n-1);###best move 
}
 
 
int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
    int n,m;
    scanf("%d%d",&n,&m);
    int a[n];
    for(int  i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    bool k=isSubset(a,m,n);
    if(k==true)
        printf("Yes\n");
    else
        printf("No\n");
    }
    return 0;
}
 
