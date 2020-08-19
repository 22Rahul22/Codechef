t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    f = 0
    ans = 0
    for i in range(n):
        if arr[i] > k:
            f = 1
            break
        else:
            if k % arr[i] == 0:
                ans = arr[i]
    if f == 1 and ans == 0:
        print(-1)
    else:
        print(ans)