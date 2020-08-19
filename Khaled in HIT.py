t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    x = n // 4
    a, b, c = arr[x], arr[2*x], arr[3*x]
    if arr.index(a) != x or arr.index(b) - arr.index(a) != x or arr.index(c) - arr.index(b) != x or n - arr.index(c) != x:
        print(-1)
    else:
        print(a, b, c)