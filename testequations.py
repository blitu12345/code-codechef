t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    s=list(map(int,raw_input().split()))
    ans=[]
    sum=0
    for j in range(len(s)):
        sum+=s[j]
    for j in range(len(s)):
        ans.append((sum/(n-1))-s[j])
    print ' '.join(str(x) for x in ans)