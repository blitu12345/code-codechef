for _ in range(input()):
    r = 103993 % 33102
    num = '3.'
    k = input()
    if k == 0:
        print '3'
        continue
    for i in range(k):
        r *= 10
        num += str(r/33102)
        r = r%33102
    print num 