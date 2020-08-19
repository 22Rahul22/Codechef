import math
t = int(input())
for _ in range(t):
    n = int(input())
    m = 0
    c = 0
    for i in range(n):
        s, p, v = map(int, input().split())
        if math.floor(p/(s+1)) * v > m:
            m = math.floor(p/(s+1)) * v
    print(m)