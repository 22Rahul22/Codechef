t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    d = []
    g = []
    if 1 not in a or 0 not in a:
        print('no')
    else:
        for i in range(n):
            if a[i] == 1:
                g.append(p[i])
            else:
                d.append(p[i])
        if min(d) + min(g) <= 100 - s:
            print('yes')
        else:
            print('no')
