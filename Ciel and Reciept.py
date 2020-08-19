import math
t = int(input())
for _ in range(t):
    p = int(input())
    c = 0
    t = True
    while t:
        x = int(math.log2(p))
        if p - math.pow(2, x) == 0 and x < 12:
            c += 1
            t = False
        else:
            if x >= 12:
                p -= math.pow(2, 11)
            else:
                p -= math.pow(2, x)
            c += 1
    print(c)