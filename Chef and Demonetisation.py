t = int(input())
for _ in range(t):
    s, n = map(int, input().split())
    a = []
    c = 0
    if (s % 2 == 0 and s <= n) or s == 1:
        print(1)
    else:
        if s % 2 != 0:
            s -= 1
            c += 1
        while s != 0:
            c += s // n
            s -= n * (s//n)
            n = s % n
        print(c)