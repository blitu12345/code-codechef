val1 = raw_input()
output = list()
t = int(val1)
for i in range(t) :
    val2 = raw_input()
    n = int(val2)
    if n%4==1 :
    	output.append('ALICE')
    else :
    	output.append('BOB')
for i in range(t) :
    print output[i] 