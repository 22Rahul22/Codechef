t = int(input())
for _ in range(t):
    n = int(input())
    m1 = 0
    m2 = 0
    m3 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    for i in range(n):
        a, b, c = list(map(int, input().split()))
        if b == 1:
            if m1 < c :
                m1 = c
                c1 = a
            elif m1 == c:
                if c1 > a:
                    c1 = a
        if b == 2:
            if m2 < c :
                m2 = c
                c2 = a
            elif m2 == c:
                if c2 > a:
                    c2 = a
        if b == 3:
            if m3 < c :
                m3 = c
                c3 = a
            elif m3 == c:
                if c3 > a:
                    c3 = a
    print(m1, c1)
    print(m2, c2)
    print(m3, c3)