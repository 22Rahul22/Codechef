t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    x = n * n
    y = arr.count(a) * arr.count(b)
    m = y / x
    print("%.10f" %m)