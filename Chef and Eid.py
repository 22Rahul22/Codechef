t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    a = 1000000000000000000
    for i in range(n-1):
        if arr[i + 1] - arr[i] <= a:
            a = arr[i + 1] - arr[i]
    print(a)