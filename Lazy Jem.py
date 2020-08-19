t = int(input())
for _ in range(t):
    n, b, m = map(int, input().split())
    temp = n
    s = 0
    while temp > 0:
        if temp % 2 == 0:
            x = temp // 2
        else:
            x = (temp + 1) // 2
        s += (x * m) + b
        m *= 2
        temp -= x
    print(s-b)
