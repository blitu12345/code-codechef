times = int(raw_input())
while times>0:
    times-=1
    n,w = list(map(int,raw_input().split()))
    p=0
    c=0
    t = [0 for i in range(n)]
    po = [0 for i in range(n)]
    for i in range(n):
        c,p,t[i] = list(map(int,raw_input().split()))
        po[i] =c*p
    dp = [[0]*(w+1) for i in range(2)]
    
    for i in range(n):
        tlist = dp[1]
        dp[1] = dp[0]
        dp[0] = tlist
        for j in range(w+1):
            if j>=t[i]:
                dp[1][j] = max(po[i]+dp[0][j-t[i]],dp[0][j])
            else:
                dp[1][j] = dp[0][j]
        #print "for i=="+str(i)+" dp[1] is "+str(dp[1])
        
    print dp[1][w]