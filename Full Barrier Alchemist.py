t = int(input())
for _ in range(t):
    n, h, y1, y2, l = map(int, input().split())
    c = 0
    for i in range(n):
        a, b = map(int, input().split())
        if l > 0:
            if a == 1:
                if h - y1 <= b:
                    c += 1
                else:
                    l -= 1
                    if l > 0:
                        c += 1
            else:
                if y2 >= b:
                    c += 1
                else:
                    l -= 1
                    if l > 0:
                        c += 1
    print(c)