t=input()
while(t>0):
    hh,mm=map(int,raw_input().strip().split())
    acc=0
    for i in xrange(hh):
    	for j in xrange(mm):
    		if len(set(str(i)+str(j)))==1:
    			print set(str(i)+str(j))
    			acc+=1
    print acc
    t-=1			 