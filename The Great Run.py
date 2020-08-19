t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    s = 0
    ans = 0
    for i in range(n-k+1):
        s = sum(arr[i:i+k])
        if s >= ans:
            ans = s
    print(ans)