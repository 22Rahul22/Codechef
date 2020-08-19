t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c1 = 0
    c2 = 0
    for i in range(n):
        if i % 2 == 0:
            c1 += a[i]
            c2 += b[i]
        else:
            c1 += b[i]
            c2 += a[i]
    print(min(c1, c2))