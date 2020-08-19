t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]*6
    for i in range(n):
        s = input()
        a[0] += s.count('c')
        a[1] += s.count('o')
        a[2] += s.count('d')
        a[3] += s.count('e')
        a[4] += s.count('h')
        a[5] += s.count('f')
    m = min(a[1], a[2], a[4], a[5])
    m2 = min(a[0], a[3])
    print(min(m2 // 2, m))
