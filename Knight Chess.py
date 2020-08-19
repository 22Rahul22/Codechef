t = int(input())
for _ in range(t):
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    a, b = map(int, input().split())
    f = 0
    for i in range(-1, 1):
        for j in range(-1, 1):
            q = a + i
            r = b + i
            for k in range(n):
                if (abs(q - x[k]) == 1 and abs(r - y[k]) == 2) or (abs(q - x[k]) == 2 and abs(r - y[k]) == 1):
                    f = 1
                    break
            if f == 0:
                break
    if f == 0:
        print('NO')
    else:
        print('YES')