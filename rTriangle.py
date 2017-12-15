from math import*
t=input()
while(t):
	t-=1
	h,s=map(float,raw_input().split())
	try:
		b=sqrt(((h**2)+sqrt(h**4-(16*s**2)))/2)
		a=sqrt((h**2)-(b**2))
		h=sqrt(a**2+b**2)
		if(a>b):
			print ("%0.6f %0.6f %0.6f")%(b,a,h)
		else:
			print ("%0.6f %0.6f %0.6f")%(a,b,h)
	except:
		print -1