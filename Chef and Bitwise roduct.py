import math


def fun(p, q, r):
    return (p & r) * (q & r)


#for i in range(80, 90):
 #   print(math.log2(i), math.ceil(math.log2(i)))
t = int(input())
for _ in range(t):
    x, y, l, r = map(int, input().split())
    if x == 0 or y == 0:
        print(0)
    elif l == 0 and r >= 2*max(x, y):
        print(x | y)
    elif r >= max(x, y):
        print(max(x, y))




