import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    b = []
    for i in range(3):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    c = []
    for i in range(3):
        for j in range(i+1, 3):
            c.append(math.sqrt(pow((a[i]-a[j]), 2)+pow((b[i]-b[j]), 2)))
    z = 0
    for i in c:
        if i <= n:
            z += 1
    if z >= 2:
        print('yes')
    else:
        print('no')