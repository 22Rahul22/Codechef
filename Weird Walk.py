t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s1 = 0
    s2 = 0
    i = 0
    weird = 0
    while i < n:
        if s1 == s2 and a[i] == b[i]:
            s1 += a[i]
            s2 += a[i]
            weird += a[i]
        else:
            s1 += a[i]
            s2 += b[i]
        i += 1
    print(weird)