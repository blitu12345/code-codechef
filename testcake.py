T = int(raw_input())
while T:
    N = int(raw_input())
    if 360 % N == 0: print 'y',
    else: print 'n',
    if N <= 360: print 'y',
    else: print 'n',
    if (N * ( N + 1 ))/2 <= 360: print 'y',
    else: print 'n',
    print
    T-=1