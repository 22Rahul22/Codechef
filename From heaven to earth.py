import math
t = int(input())
for _ in range(t):
    n, v1, v2 = map(int, input().split())
    x = math.sqrt(2) * n
    y = 2 * n
    x /= v1
    y /= v2
    if x < y:
        print("Stairs")
    else:
        print("Elevator")