t=int(raw_input())
while t>0:
    n=int(raw_input())
    time=0
    while n>0:
        x,i,f=map(int,raw_input().split())
        if x>time:
            time+=x-time
        elif (time-x)%f:
            time+=f-(time-x)%f
        time+=i
        n-=1
    print time
    t-=1  