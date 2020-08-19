t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    for i in range(n):
        x = arr[i] % k
        if x <= k // 2 and arr[i] - x != 0:
            arr[i] -= x
            s += x
        else:
            arr[i] += k - x
            s += k - x
    print(s)
