t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    for i in range(n):
        p, q, d = map(int, input().split())
        a = p + (p * d / 100)
        a -= (a * d ) / 100
        s += (p - a) * q
    print(s)