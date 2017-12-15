t = int(input())
while t>0:
    s = list(raw_input())
    l = len(s)
    i=0
    flag=1
    while i<int((l+1)/2):
        if not s[i]==s[l-1-i]:
            flag=2
            break
        i+=1
    print(flag)
    t-=1