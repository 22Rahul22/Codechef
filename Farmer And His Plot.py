t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    i = 1
    while i <= m and i <= n:
        if m % i == 0 and n % i == 0:
            h = i
        i += 1
    print((m*n)//(h*h))