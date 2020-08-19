t = int(input())
for _ in range(t):
    n = int(input())
    m = 0
    for i in range(n):
        a = int(input())
        if a >= m:
            m = a
    print(m)