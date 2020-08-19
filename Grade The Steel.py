t = int(input())
for _ in range(t):
    h, c, t = input().split()
    h = int(h)
    c = float(c)
    t = int(t)
    f1 = f2 = f3 = 0
    z = 0
    if h > 50:
        f1 = 1
        z += 1
    if c < 0.7:
        f2 = 1
        z += 1
    if t > 5600:
        f3 = 1
        z += 1
    if z == 3:
        print(10)
    elif f1 == 1 and f2 == 1 and f3 == 0:
        print(9)
    elif f2 == 1 and f3 == 1 and f1 == 0:
        print(8)
    elif f1 == 1 and f3 == 1 and f2 == 0:
        print(7)
    elif z == 1:
        print(6)
    else:
        print(5)
