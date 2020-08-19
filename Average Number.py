t = int(input())
for _ in range(t):
    n, k, v = map(int, input().split())
    arr = list(map(int, input().split()))
    s = sum(arr)
    x = v * (n + k) - s
    if x % k != 0 or x < 0:
        print(-1)
    elif x % k == 0:
        print(x // k)