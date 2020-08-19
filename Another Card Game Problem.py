t = int(input())
for _ in range(t):
    n = input().split()
    a = len(n[0])
    b = len(n[1])
    if a == 1 and b > 1:
        print(0, 1)
    elif a > 1 and b == 1:
        print(1, 1)
    elif a == 1 and b == 1:
        print(1, 1)
    elif a > 1 and b > 1:
        pc, pr = map(int, n)
        if pc % 9 == 0:
            x = pc // 9
        else:
            x = (pc // 9) + 1
        if pr % 9 == 0:
            y = pr // 9
        else:
            y = (pr // 9) + 1
        if x < y:
            print(0, x)
        else:
            print(1, y)