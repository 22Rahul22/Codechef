t = int(input())
for _ in range(t):
    n = int(input())
    x = []
    y = []
    for i in range(4*n-1):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    x1 = 0
    y1 = 0
    c1 = 0
    z = 0
    i = 0
    while i < len(x):
        c1 = 0
        for j in range(i, len(x)):
            if x[i] == x[j]:
                c1 += 1
            else:
                z = j
                break
        if c1 % 2 != 0:
            x1 = x[i]
            break
        else:
            i = z
    i = 0
    while i < len(y):
        c1 = 0
        for j in range(i, len(y)):
            if y[i] == y[j]:
                c1 += 1
            else:
                z = j
                break
        if c1 % 2 != 0:
            y1 = y[i]
            break
        else:
            i = z
    print(x1, y1)