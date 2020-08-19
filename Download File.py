t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    p = 0
    for i in range(n):
        t, d = map(int, input().split())
        temp = k
        if k == 0:
            p += t * d
        else:
            if t <= k:
                k -= t
            elif t > k:
                t -= k
                k = 0
                p += t*d
    print(p)