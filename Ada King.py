t = int(input())
for _ in range(t):
    r, c, k = map(int, input().split())
    if r + k > 8:
        r1 = 8
    else:
        r1 = r + k
    if r - k < 1:
        r2 = 1
    else:
        r2 = r - k
    if c + k > 8:
        c1 = 8
    else:
        c1 = c + k
    if c - k < 1:
        c2 = 1
    else:
        c2 = c - k
    print(abs(c1 - c2 + 1) * abs(r1 - r2 + 1))