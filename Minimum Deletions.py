import math
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c = 0
    f = arr[0]
    for i in range(1, n):
        f = math.gcd(arr[i], f)
        if f == 1:
            break
    if f == 1:
        print(0)
    else:
        print(-1)