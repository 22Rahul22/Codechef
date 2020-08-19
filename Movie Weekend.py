t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    a = []
    b = []
    for i in range(n):
        a.append(l[i] * r[i])
    m = max(a)
    s = 0
    if a.count(m) != 1:
        for i in range(len(a)):
            if m == a[i]:
                b.append(i)
        for i in b:
            if s < r[i]:
                s = r[i]
                x = i
        print(x+1)
    else:
        print(a.index(m) + 1)