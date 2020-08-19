t = int(input())
for _ in range(t):
    tr = int(input())
    t1 = list(map(int, input().split()))
    dr = int(input())
    d1 = list(map(int, input().split()))
    ts = int(input())
    t2 = list(map(int, input().split()))
    ds = int(input())
    d2 = list(map(int, input().split()))
    f = 1
    for i in range(ts):
        if t2[i] not in t1:
            f = 0
            break
    for i in range(ds):
        if d2[i] not in d1:
            f = 0
            break
    if f == 1:
        print('yes')
    else:
        print('no')