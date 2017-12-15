t=input()
while(t>0):
	t-=1
	s=raw_input()
	count=1;day=0;max1=1;i=0;n=len(s)
	while(i<n):
		#print "i"
		#print i
		#print s[i]
		if(s[i]=='.'):
			#print "if-1"
			count+=1
			#print "count"
			#print count
		if( max1< count and s[i]!='.' ):
			#print "if-2"
			day+=1
			max1=count
			count=1
		if(max1>=count and s[i]!='.'):
			#print "if-3"
			count=1
		#print "count"
		#print count
		#print "max1"
		#print max1
		#print "day"
		#print day
		i+=1
	if(max1<count):
		day+=1
	print day


###awesome code

#include<iostream>
using namespace std;
char s[2000000];
int main()
{
	long long int t,i,j,ans,len;
	cin >> t;
	while(t--)
	{
		len=1;
		ans=0;
		cin >> s;
		i=0;
		while(s[i] != '\0')
		{
			j=0;
			if(s[i] == '.')
			{
				while(s[i] == '.') 
				{
					i++;
					j++;
				}
				i--;
				if(j+1 > len) 
				{
					ans++;
					len = j+1;
				}
			}
			i++;
		}
		cout << ans << endl;
	}
	return(0);
}