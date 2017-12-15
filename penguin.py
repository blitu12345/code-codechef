def check(w,n,arr,stock):
	#print "func"
	#print "w,n",w,n
	if(w<0):
		#print "return----"
		return -arr[n][1]
	if(stock[w][n]>=0 or w==0 or n==0):
		return stock[w][n]
	#print "return"
	#print "w,n,c1",w-arr[n-1][0],n-1,c1
	#print "w,n,c2",w,n-1,c2
	#if(stock[w][n]!=-1):
		#return stock[w][n]
	#else:
		#stock[w][n]= 
	stock[w][n]= max(check(w-arr[n-1][0],n-1,arr,stock)+arr[n-1][1],check(w,n-1,arr,stock))
	return stock[w][n]
	#print "max1",max1

t=input()
while(t):
	t-=1
	n,w=map(int,raw_input().split())
	arr=[];stock=[[-1 for i in range(n+1)]for j in range(w+1)]
	i=0
	while(i<n):
		stock[0][i]=0
		a=map(int,raw_input().split())
		arr.append([a[2],a[0]*a[1]])
		i+=1
	i=0
	while(i<w):
		stock[i][0]=0
		i+=1
	if(n>0):
		print max(check(w-arr[n-1][0],n-1,arr,stock)+arr[n-1][1],check(w,n-1,arr,stock))
	else:
		print 0



using namespace std;
 
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	int n,w,c[101],p[101],t[101],ma=0;
	cin>>n>>w;
	int f[n+1][w+1];
	for(int i=1;i<=n;i++)
	{
	    cin>>c[i]>>p[i]>>t[i];
	}
	for(int j=0;j<=w;j++)
		f[0][j]=0;
	for(int i=1;i<=n;i++)
	{						#ab jab mein j se kkam weights mein chotu ko add lkarunga toh koi fayda nhi hoga
	    					#isiliye eq-1
	    for(int j=0;j<=w;j++)#lekin bade weights jo j>t[i] unme chotu ko add krne farak pad sakta h isisliye
	    						#isilie eq-2
	    {						#tb hme eq-2 se check krne haoga ki farak padta h ya nhi
	        if(j>=t[i])
	        {
	            f[i][j]=max(f[i-1][j-t[i]]+c[i]*p[i],f[i-1][j]);#eq-2
	        }
	        else
	        f[i][j]=f[i-1][j];#eq-1
	    }
	}
	cout<<f[n][w]<<endl;
	}
	return 0;
}
