cases = int(raw_input())
 
union_find = []
 
def find(v):
    if v == union_find[v]: return v
    return find(union_find[v])
 
def union(u, v):
    global union_find
    union_find[find(v)] = find(u)
 
 
for _ in xrange(cases):
    n,m = map(int, raw_input().split())
    setsmap = [0 for i in xrange(n)]
    union_find = [i for i in xrange(n)]
    for setindex in xrange(m):
        S = map(int, raw_input().split()[1:])
        for i in S:
            setsmap[i] |= (1<<setindex)
    
    for i in xrange(n):
        for j in xrange(i+1,n):
            if setsmap[i] == setsmap[j]:
                union(i, j)
 
    count = 0
    for i in xrange(n):
        if union_find[i] == i: count += 1
 
    print count
 