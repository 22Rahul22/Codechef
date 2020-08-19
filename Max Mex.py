t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    f = 1
    c = 0
    arr.sort()
    for i in range(min(arr),m):
        if i == arr[i]:
            c += 1
    if c != m-1:
        print(-1)
    else:
        cnt1 = 0
        for i in range(n):
            if arr[i] == m:
                cnt1 += 1
        print(n-cnt1)