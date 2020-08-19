import math
t = int(input())
for _ in range(t):
    n = int(input())
    temp = n
    c = 0
    while temp > 0:
        x = int(math.sqrt(temp))
        temp -= pow(x, 2)
        c += 1
    print(c)
