n = input()
for i in range(0,n):
	arr = raw_input()
	arr = [bin(int(x)) for x in arr.split()]
	a = arr[0][2:]
	b = arr[1][2:]	
	if a == b:
		print 0
	else:
		k = 1		
		while 1:
			if k+1 <=len(a) and k+1<=len(b):
				if a[k] == b[k]:
					k+=1
				else:
					break
			else:
				break
		print len(a) + len(b) - 2*k 