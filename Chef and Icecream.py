t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c = []
    f = 0
    for i in range(n):
        if arr[i] == 5:
            c.append(5)
        elif arr[i] == 10:
            if 5 in c:
                c.remove(5)
                c.append(10)
            else:
                f = 1
                break
        else:
            if 10 in c:
                c.remove(10)
                c.append(15)
            elif c.count(5) >= 2:
                c.remove(5)
                c.remove(5)
                c.append(15)
            else:
                f = 1
                break
    if f == 0:
        print('YES')
    else:
        print('NO')