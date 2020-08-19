t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y >= x:
        print(0)
    else:
        c = 0
        i = y
        while x > i:
            x -= 2
            c += 1
            i -= 1
        print(c)