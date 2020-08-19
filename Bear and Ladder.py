t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    m1 = m2 = 0
    if a % 2 == 0:
        m2 = a
    else:
        m1 = a
    if b % 2 == 0:
        m2 = b
    else:
        m1 = b
    i1 = (m1 - 1) / 2
    i2 = (m2 - 2) / 2
    if i1 == i2 or abs(a - b) == 2:
        print('YES')
    else:
        print('NO')